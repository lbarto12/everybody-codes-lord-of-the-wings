from collections import Counter
from itertools import permutations
from math import prod

from ..load import load
from ..common import mix


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

        counts: Counter[str] = Counter()
        for row in res:
            counts.update(row)

        mx = max(mx, prod(i[1] for i in counts.most_common(3)))

    return mx


if __name__ == "__main__":
    print(solve(load(2)))
