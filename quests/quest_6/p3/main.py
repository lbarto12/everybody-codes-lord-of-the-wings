from collections import defaultdict, deque

from ..load import load


def solve(data: dict[str, list[str]]) -> int:

    flipped: dict[str, list[str]] = defaultdict(list)

    for item, ingredients in data.items():
        for ingredient in ingredients:
            flipped[ingredient].append(item)

    entries: list[str] = [i for i in flipped if i.startswith("NULL")]
    chains: defaultdict[str, set[str]] = defaultdict(set)

    for item in entries:
        start: list[str] = flipped[item]

        q: deque[str] = deque(start.copy())
        while q:
            i: str = q.popleft()
            if i in chains[item] or i.startswith("NULL"):
                continue
            chains[item].add(i)

            if i not in flipped:
                continue

            for x in flipped[i]:
                q.append(x)

    doubles: set[str] = set()
    for item_1, i_1 in chains.items():
        for item_2, i_2 in chains.items():
            if item_1 == item_2:
                continue

            doubles.update(i_1.intersection(i_2))

    return len(doubles)


if __name__ == "__main__":
    ans: int = solve(load("quests/quest_6/p3/in.txt"))
    print(ans)
