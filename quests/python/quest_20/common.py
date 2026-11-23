from collections import defaultdict
from typing import cast


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


def evaluate(expr: str) -> bool:
    return cast(bool, eval(b11_sub(expr).replace("=", "==")))


def segments(s: str) -> int:
    return sum(SEG[i] for i in s)


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

GIVE: dict[str, set[str]] = {
    "6": {"5"},
    "7": {"1"},
    "8": {"6", "9", "0", "A"},
    "9": {"3", "5"},
    "+": {"-"},
}
GET: defaultdict[str, set[str]] = defaultdict(set)
for k, v in GIVE.items():
    for i in v:
        GET[i].add(k)

SELF: dict[str, set[str]] = {
    "0": {"9", "6", "A"},
    "2": {"3"},
    "3": {"2", "5"},
    "5": {"3"},
    "6": {"9", "A", "0"},
    "9": {"6", "A", "0"},
    "A": {"6", "9", "0"},
}
