from ..load import load_p2


def solve(data: list[tuple[int, int, int]]) -> int:
    height: int = max(i[1] for i in data)

    repeated: list[tuple[int, int, int]] = []

    for x, y, w in data:
        for i in range(x, x + w):
            repeated.append((i, y, w))

    res: int = 0
    while height > 0:
        xs: set[int] = {i[0] for i in repeated if i[1] >= height}
        spread: int = max(xs) - min(xs) + 1
        res += spread
        height -= 1

    return res


if __name__ == "__main__":
    print(solve(load_p2("quests/quest_18/p2/in.txt")))
