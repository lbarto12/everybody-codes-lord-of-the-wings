from quests.quest_9.common import Plant

from ..load import load


def solve(data: list[Plant]) -> int:

    res: int = 0
    for _, growth, limit in data:
        branches: list[tuple[int, bool]] = [(0, True)]
        seconds: int = 0

        while sum(i[1] for i in branches) < limit:
            seconds += 1
            nxt: list[tuple[int, bool]] = []

            for length, isleaf in branches:
                new: int = length + 1

                if new == growth:
                    nxt += [
                        (growth // 2, False),
                        (growth // 2, isleaf),
                        (1, True),
                    ]  # stem, continuance, fork
                else:
                    nxt.append((length + 1, isleaf))

            delay = branches.copy()
            branches = nxt

        res += seconds

    return res


if __name__ == "__main__":
    ans: int = solve(load("quests/quest_9/p2/in.txt"))
    print(ans)
