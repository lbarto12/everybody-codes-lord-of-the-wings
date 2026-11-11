from copy import deepcopy

from ..load import load
from ...common import adjacent, in_bounds, getxy, setxy
from ..common import Map, Pos, count_adj, can_place_tree
from ..p2.main import solve as p2


def solve(data: Map) -> int:
    data, _ = p2(data)

    trees: set[Pos] = set()
    for y, row in enumerate(data):
        for x, c in enumerate(row):
            if c == "#" and can_place_tree(data, (x, y)):
                data[y][x] = "@"
                trees.add((x, y))

    for _ in range(2):
        check: set[Pos] = set()
        for tile in trees:
            for p in adjacent(*tile):
                if in_bounds(data, p) and getxy(data, p) == "#":
                    check.add(p)

        gen: Map = deepcopy(data)
        n: int = len(trees)
        for tile in check:
            if count_adj(data, tile, "=") == 0 and count_adj(data, tile, "@") >= 4:
                setxy(gen, tile, "@")
                trees.add(tile)
        if len(trees) == n:
            break

        data = gen

    return len(trees)


if __name__ == "__main__":
    print(solve(load(3)))
