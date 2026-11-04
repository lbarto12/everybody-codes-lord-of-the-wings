from ..load import load
from ..common import to_int


def valid(base: str, mul: str) -> bool:
    c: int = to_int(base, mul)

    for i in range(int(mul)):
        if to_int(base, str(i)) == c:
            return False

    return True


def solve(data: list[tuple[str, str]]) -> int:
    s: int = 0
    for base, mul in data:
        if valid(base, mul):
            s += to_int(base, mul)

    return s


if __name__ == "__main__":
    print(solve(load("quests/quest_3/p3/in.txt")))
