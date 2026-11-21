from ..load import load
from ..common import evaluate, segments


def solve(data: list[str]) -> int:
    return sum(segments(eq) for eq in data if evaluate(eq))


if __name__ == "__main__":
    print(solve(load("quests/quest_20/p1/in.txt")))
