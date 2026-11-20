from collections import Counter
from math import prod

from ..load import load
from ..common import mix


def solve(data: list[list[str]]) -> int:
    w, h = len(data[0][0]), len(data[0])

    res: list[list[str]] = [["" for _ in range(w)] for _ in range(h)]

    top: list[str] = data[0]
    bottom: list[str] = data[1]

    for y, row in enumerate(top):
        for x, c in enumerate(row):
            res[y][x] = mix(c, bottom[y][x])

    counts: Counter[str] = Counter()
    for row in res:
        counts.update(row)

    return prod(i[1] for i in counts.most_common(3))


if __name__ == "__main__":
    print(solve(load(1)))
