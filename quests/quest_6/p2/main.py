from collections import defaultdict, deque

from ..load import load


def solve(data: dict[str, list[str]]) -> int:

    flipped: dict[str, list[str]] = defaultdict(list)

    for item, ingredients in data.items():
        for ingredient in ingredients:
            flipped[ingredient].append(item)

    start: list[str] = flipped["NULL"]
    ingreds: set[str] = set()

    q: deque[str] = deque(start.copy())
    while q:
        i: str = q.popleft()
        if i in ingreds or i == "NULL":
            continue
        ingreds.add(i)

        if i not in flipped:
            continue

        for x in flipped[i]:
            q.append(x)

    return len(ingreds)


if __name__ == "__main__":
    ans: int = solve(load(2))
    print(ans)
