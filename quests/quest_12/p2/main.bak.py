from copy import deepcopy
from functools import cache

from quests.common import getxy, in_bounds, t_add
from quests.quest_12.common import MagmaPatch
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


def setup_spells(patch: MagmaPatch) -> dict[tuple[int, int], int]:
    return {pos: 2 for pos in patch}


def get_duplicated_cells(spells: dict[tuple[int, int], int]) -> set[tuple[int, int]]:
    return {k for k, v in spells.items() if v > 1}


def remove_spell_x(
    spells: dict[tuple[int, int], int], col: int
) -> tuple[dict[tuple[int, int], int], bool]:  # new, valid
    _new = deepcopy(spells)
    for (x, y), v in spells.items():
        if x == col:
            v -= 1
        if v < 1:
            return _new, False
        _new[x, y] = v
    return _new, True


def remove_spell_y(
    spells: dict[tuple[int, int], int], row: int
) -> tuple[dict[tuple[int, int], int], bool]:  # new, valid
    _new = deepcopy(spells)
    for (x, y), v in spells.items():
        if y == row:
            v -= 1
        if v < 1:
            return _new, False
        _new[x, y] = v
    return _new, True


def minimize(spells: dict[tuple[int, int], int]) -> int:
    total_spells: int = (max(c := {x for (x, _) in spells}) - min(c) + 1) + (
        max(c := {y for (_, y) in spells}) - min(c) + 1
    )

    seen: set[tuple[tuple[tuple[tuple[int, int], int], ...], int]] = set()

    def permute(s: dict[tuple[int, int], int], t: int) -> int:
        _hashish = (tuple((p, v) for p, v in s.items()), t)
        if _hashish in seen:
            return t
        seen.add(_hashish)

        opts: list[int] = []
        any_valid: bool = False
        for x, y in get_duplicated_cells(spells):
            r_x, valid = remove_spell_x(s, x)
            if valid:
                any_valid = True
                opts.append(permute(r_x, t - 1))
            r_y, valid = remove_spell_y(s, y)
            if valid:
                any_valid = True
                opts.append(permute(r_y, t - 1))
        if not any_valid:
            return t
        return min(opts)

    return permute(spells, total_spells)


def solve(data: list[str]) -> int:
    patches: list[MagmaPatch] = islands(data)

    # print(*patches, sep="\n")

    res: int = 0
    print(f"total patches: {len(patches)}")
    for i, patch in enumerate(patches):
        spells: dict[tuple[int, int], int] = setup_spells(patch)
        r: int = minimize(spells)
        print(f"{i}: {r}")
        res += r
        # print(spells)
        # print(minimize(spells))

    return res


if __name__ == "__main__":
    print(solve(load_from("quests/quest_12/p2/in.txt")))
