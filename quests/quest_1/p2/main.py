from ..load import load


def calc(x: int) -> int:
    return x * 4 + 4


def solve(data: list[int]) -> int:
    n: int = 1
    res: int = 0
    for outpost in data:
        while (r := calc(n)) < outpost:
            n += 1
        res += r - outpost

    return res


if __name__ == "__main__":
    print(solve(load("quests/quest_1/p2/in.txt")))
