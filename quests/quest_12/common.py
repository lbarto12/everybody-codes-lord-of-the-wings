from typing import TypeAlias

from quests.common import adjacent4, getxy, in_bounds, t_add


Dims: TypeAlias = tuple[int, int]
Pos: TypeAlias = tuple[int, int]
MagmaPatch: TypeAlias = set[Pos]
MagmaSquare: TypeAlias = tuple[Pos, Pos]


def islands(data: list[str]) -> list[MagmaPatch]:
    seen: set[Pos] = set()
    listified: list[list[str]] = list(map(list, data))

    def dfs(p: Pos, island: MagmaPatch) -> MagmaPatch:
        if not in_bounds(listified, p) or getxy(listified, p) != "#" or p in seen:
            return island
        seen.add(p)
        island.add(p)

        for p in adjacent4(p):
            island.update(dfs(p, island))

        return island

    return [
        dfs((x, y), set())
        for y, row in enumerate(listified)
        for x, c in enumerate(row)
        if c == "#" and (x, y) not in seen
    ]


def complete(patch: MagmaPatch) -> MagmaSquare:
    xs, ys = {x for (x, _) in patch}, {y for (_, y) in patch}
    return (min(xs), min(ys)), (max(xs), max(ys))


def missing(patch: MagmaPatch, total: MagmaSquare) -> MagmaPatch:
    return {
        (x, y)
        for y in range(total[0][1], total[1][1] + 1)
        for x in range(total[0][0], total[1][0] + 1)
        if (x, y) not in patch
    }


def dims(sqr: MagmaSquare) -> Dims:
    return (sqr[1][0] - sqr[0][0] + 1, sqr[1][1] - sqr[0][1] + 1)


def handle_l(total_dims: Dims, missing_dims: Dims) -> int:
    (tx, ty), (mx, my) = total_dims, missing_dims
    return min(tx, ty, (tx - mx) + (ty - my))


def contains(outer: MagmaSquare, inner: MagmaSquare) -> bool:
    ((ox_0, oy_0), (ox_1, oy_1)), ((ix_0, iy_0), (ix_1, iy_1)) = outer, inner
    return ix_0 > ox_0 and iy_0 > oy_0 and ox_1 > ix_1 and oy_1 > iy_1


def handle_donut(outer: MagmaSquare, inner: MagmaSquare) -> int:
    (w, h), (mw, mh) = dims(outer), dims(inner)
    ((ox_0, oy_0), (ox_1, oy_1)), ((ix_0, iy_0), (ix_1, iy_1)) = outer, inner
    lw, rw, th, bh = ix_0 - ox_0, ox_1 - ix_1, iy_0 - oy_0, oy_1 - iy_1

    return min(h - mh + min(lw, mh) + min(rw, mh), w - mw + min(th, mw) + min(bh, mw))
