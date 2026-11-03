from ..load import load


def solve(data: list[tuple[int, int, int, int]]) -> int:
    n: int = max([i[0] for i in data])
    times: list[tuple[int, int]] = [(0, 0)] * n
    for id, quest, part, time in data:
        cpart, ctime = times[id - 1]
        times[id - 1] = (cpart + 1, ctime + time)

    leaderboard: list[tuple[int, tuple[int, int]]] = list(
        zip(range(1, n + 1), sorted(times, key=lambda x: (-x[0], x[1])))
    )

    print(*leaderboard, sep="\n")

    res: int = sum([place * time[1] for (place, time) in leaderboard])

    return res


if __name__ == "__main__":
    print(solve(load("quest_4/p2/in.txt")))
