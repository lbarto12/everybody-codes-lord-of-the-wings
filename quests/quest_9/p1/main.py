from quests.quest_9.common import Plant

from ..load import load


def solve(data: list[Plant]) -> int:

    res: int = 0
    for _, growth, limit in data:
        branches: list[int] = [0]
        seconds: int = 0

        while sum(branches) + 1 < limit:
            seconds += 1
            nxt: list[int] = []

            for branch in branches:
                new: int = branch + 1

                if new == growth:
                    nxt += [growth // 2, growth // 2, 1]
                else:
                    nxt.append(branch + 1)

            branches = nxt

        res += seconds

    return res


if __name__ == "__main__":
    ans: int = solve(load(1))
    print(ans)
