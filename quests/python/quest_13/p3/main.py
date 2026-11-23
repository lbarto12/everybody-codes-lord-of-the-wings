from ..load import load
from ..common import Hand, solve_part


def solve(data: list[list[Hand]]) -> int:
    return solve_part(data)


if __name__ == "__main__":
    print(solve(load(3)))
