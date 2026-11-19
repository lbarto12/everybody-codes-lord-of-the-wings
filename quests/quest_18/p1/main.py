from ..load import load


def solve(data: list[tuple[int, int]]) -> int:
    height: int = max(i[1] for i in data)

    res: int = 0
    while height > 0:
        xs: set[int] = {i[0] for i in data if i[1] >= height}
        spread: int = max(xs) - min(xs) + 1
        res += spread
        print(spread)
        height -= 1

    return res


if __name__ == "__main__":
    print(solve(load("quests/quest_18/p1/in.txt")))
