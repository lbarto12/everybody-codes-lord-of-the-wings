from collections.abc import Generator, Iterable, Iterator, Sequence


def t_add[T: (int, float)](a: tuple[T, T], b: tuple[T, T]) -> tuple[T, T]:
    return a[0] + b[0], a[1] + b[1]


def adjacent(x: int, y: int) -> Generator[tuple[int, int]]:
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (i, j) == (0, 0):
                continue
            yield (x + j, y + i)


def adjacent4(p: tuple[int, int]) -> Generator[tuple[int, int]]:
    for o in {(-1, 0), (1, 0), (0, -1), (0, 1)}:
        yield t_add(p, o)


def in_bounds[T](data: list[list[T]], p: tuple[int, int]) -> bool:
    return 0 <= p[0] < len(data[0]) and 0 <= p[1] < len(data)


def getxy[T](arr: Sequence[Sequence[T]], pos: tuple[int, int]) -> T:
    return arr[pos[1]][pos[0]]


def setxy[T](arr: list[list[T]], pos: tuple[int, int], val: T):
    arr[pos[1]][pos[0]] = val


class DisjointSetUnion[T]:
    def __init__(self, items: Iterable[T]):
        self.parent: dict[T, T] = {i: i for i in items}
        self.sizes: dict[T, int] = {i: 1 for i in items}
        self.size: int = len(list(items))

    def find(self, i: T) -> T:
        if self.parent[i] == i:
            return i
        return self.find(self.parent[i])

    def union(self, i: T, j: T):
        if self.find(i) != self.find(j):
            self.parent[a := self.find(i)] = (b := self.find(j))
            self.sizes[b] += self.sizes[a]
            self.sizes[a] = 0
            self.size -= 1

    def len(self, i: T) -> int:
        return self.sizes[self.find(i)]

    def __iter__(self) -> Iterator[T]:
        return list(set(self.find(i) for i in self.parent.keys())).__iter__()

    def __len__(self) -> int:
        return self.size
