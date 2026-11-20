from collections import Counter
from itertools import permutations
from math import prod
import sys

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

    top: list[str] = data[0]
    bottom: list[str] = data[1]

    mx: int = 0
    for colors in permutations({"C", "Y", "M", "K"}):
        res: list[list[str]] = [["" for _ in range(w)] for _ in range(h)]
        for y, row in enumerate(top):
            for x, c in enumerate(row):
                res[y][x] = mix(c, colors[int(bottom[y][x]) - 1])

        c = Counter()
        for row in res:
            c.update(row)

        mx = max(mx, prod(i[1] for i in c.most_common(3)))

        print(*["".join(i) for i in res], sep="\n")
    return mx


if __name__ == "__main__":
    print(solve(load("quests/quest_19/p2/in.txt")))
