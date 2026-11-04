from ..load import load
from ...common import adjacent, getxy, in_bounds, setxy
from ..common import Map, Pos, count_adj


def solve(data: Map) -> tuple[Map, int]:
    first: Pos = (len(data[0]) // 2, len(data) // 2)
    data[first[1]][first[0]] = "#"

    land: set[Pos] = {first}
    new_land: set[Pos] = {first}

    while True:
        gen: Map = [i[:] for i in data]
        next_loop: set[Pos] = set()

        for pos in new_land:
            if count_adj(data, pos) >= 5 or getxy(data, pos) == "#":
                setxy(gen, pos, "#")
                land.add(pos)
                for nxt in adjacent(*pos):
                    if in_bounds(data, nxt) and getxy(data, nxt) != "#":
                        next_loop.add(nxt)

        if len(next_loop) == 0:
            break
        new_land = next_loop

        data = gen

    data = [[i if i == "#" else "." for i in row] for row in data]

    return data, len(land)


if __name__ == "__main__":
    _, ans = solve(load("quests/quest_5/p1/in.txt"))
    print(ans)
