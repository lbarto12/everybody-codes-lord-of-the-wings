from ..load import load
from ..common import to_int


def solve(data: list[tuple[str, str]]) -> int:
    return sum(to_int(base, mul) for base, mul in data)


if __name__ == "__main__":
    print(solve(load(2)))
