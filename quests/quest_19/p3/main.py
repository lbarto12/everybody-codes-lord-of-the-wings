from collections import Counter
from itertools import permutations
from math import prod

from ..load import load_p3


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


# C -> B, G, C
# M -> B, R, M
# Y -> G, R, Y


def get_for(r: int, g: int, b: int) -> str:
    m: int = min(r, g, b)
    if m == r:
        return "R"
    if m == g:
        return "G"
    if m == b:
        return "B"
    return "na"


def spent(c: dict[str, int]) -> bool:
    return c["C"] == c["M"] == c["Y"] == 0


def solve(data: list[str]) -> int:
    w, h = len(data[0][0]), len(data[0])

    cs: Counter[str] = Counter()
    for row in data:
        cs.update(row)
    print(cs)

    r = g = b = 0

    counts = dict(cs)

    while not spent(counts):
        print(counts)
        for c in ["R", "G", "B"]:
            if spent(counts):
                break
            if c == "R":
                if counts["M"] > counts["Y"] >= 0:
                    counts["M"] -= 1
                    r += 1
                else:
                    counts["Y"] -= 1
                    r += 1
            elif c == "G":
                if counts["C"] > counts["Y"] >= 0:
                    counts["C"] -= 1
                    g += 1
                else:
                    counts["Y"] -= 1
                    g += 1
            elif c == "B":
                if counts["C"] > counts["M"] >= 0:
                    counts["C"] -= 1
                    b += 1
                else:
                    counts["M"] -= 1
                    b += 1

    print(f"{r=}, {g=}, {b=}")

    return r * g * b


if __name__ == "__main__":
    print(solve(load_p3("quests/quest_19/p3/in.txt")))
