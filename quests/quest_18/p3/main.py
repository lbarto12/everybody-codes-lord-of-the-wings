from ..load import load_p2


def solve(data: list[tuple[int, int, int]]) -> int:
    mx: int = max(i[1] for i in data)
    height: int = 1

    li = 0
    ri = -1

    res: int = 0
    while height <= mx:
        while data[li][1] < height:
            li += 1

        while data[ri][1] < height:
            ri -= 1

        left, right = data[li], data[ri]

        spread: int = right[0] + right[2] - left[0]
        res += spread
        height += 1

    return res


if __name__ == "__main__":
    print(solve(load_p2("quests/quest_18/p3/in.txt")))
