from ast import TypeVar
from collections.abc import Generator
from typing import TypeAlias, TypeVarTuple


Map: TypeAlias = list[list[str]]
Pos: TypeAlias = tuple[int, int]

tupT = TypeVarTuple("tupT")
T = TypeVar("T")


def t_add(*args: tuple[int, ...]) -> tuple[int, ...]:
    if not len({len(i) for i in args}) == 1:
        raise ValueError("Tuple Length Mismatch")
    return tuple(sum(a[i] for a in args) for i in range(len(args[0])))


def adjacent(x: int, y: int) -> Generator[tuple[int, int]]:
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (i, j) == (0, 0):
                continue
            yield (x + j, y + i)


def count_adj(data: list[list[str]], p: tuple[int, int], cset: str = "#1") -> int:
    return sum(data[y][x] in cset for x, y in adjacent(*p) if in_bounds(data, (x, y)))


def in_bounds(data: list[list[str]], p: tuple[int, int]) -> bool:
    return 0 <= p[0] < len(data[0]) and 0 <= p[1] < len(data)


def any_water(data: list[list[str]], p: tuple[int, int]) -> bool:
    return any(
        data[y][x] == "." if in_bounds(data, (x, y)) else True for x, y in adjacent(*p)
    )


def can_place_tree(data: list[list[str]], p: tuple[int, int]) -> bool:
    cancel: set[int] = {-2, 2}
    for y in range(-2, 3):
        for x in range(-2, 3):
            if all(i in cancel for i in {x, y}):
                continue
            pos: tuple[int, int] = (x + p[0], y + p[1])
            if not in_bounds(data, pos) or data[pos[1]][pos[0]] not in "#@":
                return False
    return True
