from ..load import load
from ...common import adjacent, getxy, in_bounds, setxy
from ..common import Map, Pos, count_adj, any_water
from ..p1.main import solve as p1


def solve(data: Map) -> tuple[Map, int]:
    data, _ = p1(data)

    edge_tiles: set[Pos] = set()
    initial_beach: Map = [i[:] for i in data]
    for y, row in enumerate(data):
        for x, c in enumerate(row):
            if c == "#" and any_water(data, (x, y)):
                edge_tiles.add((x, y))
                initial_beach[y][x] = "="
    data = initial_beach

    sand: set[Pos] = set(edge_tiles)
    while True:
        check: set[Pos] = set()
        for s in sand:
            for pos in adjacent(*s):
                if in_bounds(data, pos) and getxy(data, pos) == "#":
                    check.add(pos)

        gen: Map = [i[:] for i in data]
        n: int = len(sand)
        for tile in check:
            if count_adj(data, tile, "=") >= 5:
                setxy(gen, tile, "=")
                sand.add(tile)
        if len(sand) == n:
            break

        data = gen

    return data, len(sand)


if __name__ == "__main__":
    _, ans = solve(load(2))
    print(ans)
