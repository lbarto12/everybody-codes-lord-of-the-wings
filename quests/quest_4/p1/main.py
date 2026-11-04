from ..load import load


def solve(data: list[tuple[int, int, int, int]]) -> int:
    n: int = max([i[0] for i in data])
    times: list[int] = [0] * n
    for id, _, _, time in data:
        times[id - 1] += time

    res: int = sum(
        [place * time for (place, time) in zip(range(1, n + 1), sorted(times))]
    )

    return res


if __name__ == "__main__":
    print(solve(load("quests/quest_4/p1/in.txt")))
