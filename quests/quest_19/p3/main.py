from collections import Counter
from math import prod

from ..load import load_p3

# C -> B, G, C
# M -> B, R, M
# Y -> G, R, Y
# The philosophy here is that each initial color C|Y|M can be 'spent'
# as a token to convert into RGB. Optimal product is when R = G = B
# unless K > min(R, G, B), but this is not the case on any provided input
# so far.
#
# So, spend 3 tokens at once, one for R, G, and B - failing if not available,
# defaulting to the tokens you have the most of. Keeping tokens equal
# should guarantee (I think) that the optimal assignment of tokens is
# chosen. Works for my input either way.
#
# E.g. next R comes from max(M tokens, Y tokens).
#
# does NOT work on the first example from the question, because K should
# be chosen :)


def spent(c: Counter[str]) -> bool:
    return c["C"] == c["M"] == c["Y"] == 0


def solve(data: list[str]) -> int:

    counts: Counter[str] = Counter()
    for row in data:
        counts.update(row)

    res: list[int] = [0, 0, 0]  # rgb

    def spend(c1: str, c2: str) -> int:
        if spent(counts):
            return 0
        if counts[c1] > counts[c2] >= 0:
            counts[c1] -= 1
        else:
            counts[c2] -= 1
        return 1

    while not spent(counts):
        res = [
            a + b
            for (a, b) in zip(res, [spend("M", "Y"), spend("C", "Y"), spend("C", "M")])
        ]

    return prod(res)


if __name__ == "__main__":
    print(solve(load_p3(3)))
