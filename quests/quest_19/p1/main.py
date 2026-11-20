from collections import Counter
from math import prod

from ..load import load


def mix(a: str, b: str) -> str:
    if "K" in {a, b}:
        return "K"
    if {a, b} == {"C", "M"}:
        return "B"
    if {a, b} == {"C", "Y"}:
        return "G"
    if {a, b} == {"M", "Y"}:
        return "R"
    return a


def solve(data: list[list[str]]) -> int:
    w, h = len(data[0][0]), len(data[0])

    res: list[list[str]] = [["" for _ in range(w)] for _ in range(h)]

    top: list[str] = data[0]
    bottom: list[str] = data[1]

    for y, row in enumerate(top):
        for x, c in enumerate(row):
            res[y][x] = mix(c, bottom[y][x])

    c = Counter()
    for row in res:
        c.update(row)

    print(*["".join(i) for i in res], sep="\n")

    return prod(i[1] for i in c.most_common(3))


if __name__ == "__main__":
    print(solve(load("quests/quest_19/p1/in.txt")))
