from ast import TypeVar
from collections.abc import Generator

T = TypeVar("T")


def adjacent(x: int, y: int) -> Generator[tuple[int, int]]:
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (i, j) == (0, 0):
                continue
            yield (x + j, y + i)


def in_bounds[T](data: list[list[T]], p: tuple[int, int]) -> bool:
    return 0 <= p[0] < len(data[0]) and 0 <= p[1] < len(data)
