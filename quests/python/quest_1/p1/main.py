# from quests.load import EverybodyCodesAPI

from ..load import load


def solve(data: list[int]) -> int:
    n: int = 1
    res: int = 0
    for outpost in data:
        while (r := n**2) < outpost:
            n += 1
        res += r - outpost

    return res


if __name__ == "__main__":
    print(solve(load(1)))
    # print(EverybodyCodesAPI().submit(1, 1, solve(load(1))))
