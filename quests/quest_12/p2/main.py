from quests.common import getxy, in_bounds, t_add
from quests.quest_12.common import MagmaPatch, MagmaSquare
from quests.quest_12.load import load_from


def islands(data: list[str]) -> list[MagmaPatch]:
    seen: set[tuple[int, int]] = set()

    def dfs(p: tuple[int, int], island: MagmaPatch) -> MagmaPatch:
        if (
            not in_bounds(list(map(list, data)), p)
            or getxy(data, p) != "#"
            or p in seen
        ):
            return island
        seen.add(p)
        island.add(p)

        return island.union(dfs(t_add(p, (-1, 0)), island)).union(
            dfs(t_add(p, (1, 0)), island).union(
                dfs(t_add(p, (0, 1)), island).union(dfs(t_add(p, (0, -1)), island))
            )
        )

    res: list[MagmaPatch] = []
    for y, row in enumerate(data):
        for x, c in enumerate(row):
            if c == "#" and (x, y) not in seen:
                res.append(dfs((x, y), set()))

    return res


def complete(patch: MagmaPatch) -> MagmaSquare:
    xs, ys = {x for (x, _) in patch}, {y for (_, y) in patch}
    return (min(xs), min(ys)), (max(xs), max(ys))


def missing(patch: MagmaPatch, total: MagmaSquare) -> MagmaPatch:
    sqr: MagmaPatch = set()

    for x in range(total[0][0], total[1][0] + 1):
        for y in range(total[0][1], total[1][1] + 1):
            if (x, y) not in patch:
                sqr.add((x, y))

    return sqr


def dims(sqr: MagmaSquare) -> tuple[int, int]:
    return (sqr[1][0] - sqr[0][0] + 1, sqr[1][1] - sqr[0][1] + 1)


def solve(data: list[str]) -> int:
    patches: list[MagmaPatch] = islands(data)

    res: int = 0
    for i, patch in enumerate(patches):
        total = complete(patch)
        total_dims = dims(total)
        spells: int = min(*total_dims)
        missing_patch = missing(patch, total)
        if not missing_patch:
            res += spells
            continue
        missing_sqr = complete(missing_patch)
        missing_dims = dims(missing_sqr)

        tx, ty = total_dims
        mx, my = missing_dims

        spells = min(tx, ty, (tx - mx) + (ty - my))
        res += spells

    return res


if __name__ == "__main__":
    print(solve(load_from("quests/quest_12/p2/in.txt")))
