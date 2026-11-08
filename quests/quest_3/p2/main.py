from ..load import load
from ..common import to_int


def solve(data: list[tuple[str, str]]) -> int:
    s: int = 0
    for base, mul in data:
        s += to_int(base, mul)

    return s


if __name__ == "__main__":
    print(solve(load(2)))
