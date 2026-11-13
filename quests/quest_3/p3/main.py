from ..load import load
from ..common import to_int


def valid(base: str, mul: str) -> bool:
    c: int = to_int(base, mul)
    return not any(to_int(base, str(i)) == c for i in range(int(mul)))


def solve(data: list[tuple[str, str]]) -> int:
    return sum(to_int(base, mul) for base, mul in data if valid(base, mul))


if __name__ == "__main__":
    print(solve(load(3)))
