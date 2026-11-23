from collections import deque


def bfs(data: dict[str, list[str]], ingredients: set[str], initial: list[str]) -> int:
    q: deque[str] = deque(initial.copy())
    while q:
        i: str = q.popleft()
        if i in ingredients or i == "NULL":
            continue
        ingredients.add(i)

        if i not in data:
            continue

        for x in data[i]:
            q.append(x)

    return len(ingredients)
