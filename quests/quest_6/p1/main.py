from collections import deque

from ..load import load


def solve(data: dict[str, list[str]]) -> int:
    print(*data.items(), sep="\n")

    start: list[str] = data["NULL"]
    ingreds: set[str] = set()

    q: deque[str] = deque(start.copy())
    while q:
        i: str = q.popleft()
        if i in ingreds or i == "NULL":
            continue
        ingreds.add(i)

        if i not in data:
            continue

        for x in data[i]:
            q.append(x)

    print(ingreds)

    return len(ingreds)


if __name__ == "__main__":
    ans: int = solve(load("quests/quest_6/p1/in.txt"))
    print(ans)
