from collections import deque

from ..load import load


def solve(data: dict[str, list[str]]) -> int:
    print(*data.items(), sep="\n")

    start = data["NULL"]
    ingreds = set()

    q = deque(start.copy())
    while q:
        i = q.popleft()
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
    ans = solve(load("quests/quest_6/p1/in.txt"))
    print(ans)
