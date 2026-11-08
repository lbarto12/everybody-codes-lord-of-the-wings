from http.cookiejar import Cookie
import os
from typing import cast

from cryptography.hazmat.primitives.ciphers import (
    Cipher,
    CipherContext,
    algorithms,
    modes,
)
from cryptography.hazmat.primitives.padding import PaddingContext
from cryptography.hazmat.primitives import padding
from dotenv import load_dotenv
import requests


class EverybodyCodesAPI:
    def __init__(self) -> None:
        if not load_dotenv():
            raise Exception("Failed to load env")

        session_token: str | None = os.getenv("SESSION")
        if not session_token:
            raise Exception("No session token found")

        self.__session: requests.Session = requests.Session()

        cookie: Cookie | None = self.__session.cookies.set(
            "everybody-codes", session_token, domain=".everybody.codes"
        )
        if not cookie:
            raise Exception("Failed to apply cookie")

        result: requests.Response = self.__session.get(
            "https://api.everybody.codes/user/me"
        )
        result.raise_for_status()

        data: dict[str, str] = cast(dict[str, str], result.json())
        if "seed" not in data:
            raise Exception("Not logged in: SESSION cookie is invalid or expired")

        self.__seed: str = data["seed"]

    def __get_aes_keys(self, quest: int) -> dict[int, str]:
        response: requests.Response = self.__session.get(
            f"https://api.everybody.codes/event/2026/quest/{quest}"
        )
        response.raise_for_status()

        marshalled: dict[str, str] = cast(dict[str, str], response.json())

        result: dict[int, str] = {
            int(k[-1]): v for k, v in marshalled.items() if k.startswith("key")
        }

        return result

    def __decrypt_inputs(
        self, encrypted: dict[int, str], keys: dict[int, str]
    ) -> dict[int, str]:
        result: dict[int, str] = {}

        for problem, e_input in encrypted.items():
            if (key := keys.get(problem)) is not None:
                cipher: Cipher[modes.CBC] = Cipher(
                    algorithms.AES(key.encode()), modes.CBC(key[:16].encode())
                )
                decryptor: CipherContext = cipher.decryptor()
                padded: bytes = (
                    decryptor.update(bytes.fromhex(e_input)) + decryptor.finalize()
                )
                unpadder: PaddingContext = padding.PKCS7(128).unpadder()
                decrypted: bytes = unpadder.update(padded) + unpadder.finalize()

                result[problem] = decrypted.decode("utf-8")

        return result

    def get_input(self, quest: int) -> dict[int, str]:
        response: requests.Response = self.__session.get(
            f"https://everybody.codes/assets/2026/{quest}/input/{self.__seed}.json"
        )
        response.raise_for_status()

        encrypted: dict[int, str] = {
            int(k): v for k, v in cast(dict[str, str], response.json()).items()
        }

        keys: dict[int, str] = self.__get_aes_keys(quest)

        inputs: dict[int, str] = self.__decrypt_inputs(encrypted, keys)

        return inputs

    def submit(self, quest: int, part: int, answer: int) -> str:
        print(f"submitting to Quest {quest}, Part {part} => {answer}")
        response: requests.Response = self.__session.post(
            f"https://api.everybody.codes/event/2026/quest/{quest}/part/{part}/answer",
            json={"answer": str(answer)},
        )

        if response.status_code == 409:
            return "already solved"
        if not response.ok:
            raise Exception(
                f"Submit to quest {quest} part {part} failed: {response.status_code} {response.text}"
            )

        data: dict[str, bool | str] = cast(dict[str, bool | str], response.json())
        verdict: str = "correct" if data.get("correct") else "wrong"
        return f"{verdict}: {data.get('message', '')}"
