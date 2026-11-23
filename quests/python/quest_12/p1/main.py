from ..load import load
from ..common import MagmaSquare, complete, islands


def solve(data: list[str]) -> int:
    patches: list[MagmaSquare] = [complete(i) for i in islands(data)]
    return sum(min(x2 - x1 + 1, y2 - y1 + 1) for (x1, y1), (x2, y2) in patches)


if __name__ == "__main__":
    print(solve(load(1)))
