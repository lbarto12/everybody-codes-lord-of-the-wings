from collections import defaultdict

from quests.quest_6.common import bfs

from ..load import load


def solve(data: dict[str, list[str]]) -> int:
    flipped: dict[str, list[str]] = defaultdict(list)

    for item, ingredients in data.items():
        for ingredient in ingredients:
            flipped[ingredient].append(item)

    start: list[str] = flipped["NULL"]
    ingreds: set[str] = set()

    return bfs(flipped, ingreds, start)


if __name__ == "__main__":
    ans: int = solve(load(2))
    print(ans)
