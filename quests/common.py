from collections.abc import Generator, Sequence


def t_add[T: (int, float)](a: tuple[T, T], b: tuple[T, T]) -> tuple[T, T]:
    return a[0] + b[0], a[1] + b[1]


def adjacent(x: int, y: int) -> Generator[tuple[int, int]]:
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (i, j) == (0, 0):
                continue
            yield (x + j, y + i)


def in_bounds[T](data: list[list[T]], p: tuple[int, int]) -> bool:
    return 0 <= p[0] < len(data[0]) and 0 <= p[1] < len(data)


def getxy[T](arr: Sequence[Sequence[T]], pos: tuple[int, int]) -> T:
    return arr[pos[1]][pos[0]]


def setxy[T](arr: list[list[T]], pos: tuple[int, int], val: T):
    arr[pos[1]][pos[0]] = val
