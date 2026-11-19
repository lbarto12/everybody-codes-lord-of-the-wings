from quests.quest_18.common import calc_with_width

from ..load import load


def solve(data: list[tuple[int, int, int]]) -> int:
    return calc_with_width(data)


if __name__ == "__main__":
    print(solve(load(2)))
