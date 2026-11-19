from ..load import load_p2


def solve(data: list[tuple[int, int, int]]) -> int:
    mx: int = max(i[1] for i in data)

    height: int = 1
    li, ri = 0, -1

    res: int = 0
    while height <= mx:
        while data[li][1] < height:
            li += 1

        while data[ri][1] < height:
            ri -= 1

        (x1, y1, _), (x2, y2, w2) = data[li], data[ri]
        spread: int = x2 + w2 - x1
        run: int = min(y1, y2) - height + 1

        res += spread * run
        height += run

    return res


if __name__ == "__main__":
    print(solve(load_p2("quests/quest_18/p3/in.txt")))
