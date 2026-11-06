import re
from typing import cast

from .common import Plant


def load(path: str) -> list[Plant]:
    with open(path) as file:
        lines: list[str] = [i.strip() for i in file.readlines()]

        result: list[Plant] = []
        for line in lines:
            match = cast(
                tuple[str, str, str],
                re.findall(r"id=(\d+), growth=(\d+), limit=(\d+)", line)[0],
            )
            id, growth, limit = match
            result.append((int(id), int(growth), int(limit)))
        return result
