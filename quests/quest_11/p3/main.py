from collections.abc import Generator
from copy import deepcopy

from ..load import load
from ..common import setup, get_load, apply_shortcut


def generate_pairings(lst: list[int]) -> Generator[list[tuple[int, int]]]:
    if not lst:
        yield []
        return

    first: int = lst[0]

    for i in range(1, len(lst)):
        pair: tuple[int, int] = (first, lst[i])
        remaining: list[int] = lst[1:i] + lst[i + 1 :]

        for rest in generate_pairings(remaining):
            yield [pair] + rest


def solve(portals: int, shortcuts: list[tuple[int, int]]) -> int:
    states, initial_load = setup(portals, shortcuts)

    res: int = initial_load

    for start in range(1, (step := portals // 8) + 1):
        positions: set[int] = set()
        while start <= portals:
            positions.add(start)
            start += step

        for a, b, c, d in generate_pairings(list(positions)):
            cpy: dict[tuple[int, int], int] = deepcopy(states)
            tst: int = get_load(
                apply_shortcut(
                    apply_shortcut(apply_shortcut(apply_shortcut(cpy, a), b), c), d
                )
            )

            if tst < res:
                res = tst

    return initial_load - res


if __name__ == "__main__":
    print(solve(*load(3)))
