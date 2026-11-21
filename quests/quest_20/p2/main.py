from ..load import load

SEG: dict[str, int] = {
    "0": 6,
    "1": 2,
    "2": 5,
    "3": 5,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 3,
    "8": 7,
    "9": 6,
    "+": 2,
    "-": 1,
    "=": 2,
    "A": 6,
    " ": 0,
}


def to_b11(n: int) -> str:
    if n == 0:
        return "0"

    digits = "0123456789A"
    sign: str = "-" if n < 0 else ""
    n = abs(n)

    res: list[str] = []
    while n > 0:
        n, rem = divmod(n, 11)
        res.append(digits[rem])

    return sign + "".join(reversed(res))


def b11_sub(s: str) -> str:
    blocks: list[str] = s.split(" ")
    for i, b in enumerate(blocks):
        if b in {"+", "-", "="}:
            continue
        blocks[i] = str(int(b, 11))

    return " ".join(blocks)


def solve(data: list[str]) -> str:
    res: int = 0
    for eq in data:
        if eval(b11_sub(eq).replace("=", "==")):
            res += sum(SEG[i] for i in eq)

    return to_b11(res)


if __name__ == "__main__":
    print(solve(load("quests/quest_20/p2/in.txt")))
