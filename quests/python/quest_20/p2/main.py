from ..load import load
from ..common import evaluate, segments, to_b11


def solve(data: list[str]) -> str:
    return to_b11(sum(segments(eq) for eq in data if evaluate(eq)))


if __name__ == "__main__":
    print(solve(load(2)))
