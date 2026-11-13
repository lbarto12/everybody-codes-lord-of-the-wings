from ..load import load
from ..common import solve_from


def solve(data: list[list[tuple[int, int]]]) -> int:
    return solve_from(data)


if __name__ == "__main__":
    print(solve(load(3)))
