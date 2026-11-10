from collections.abc import Generator
from copy import deepcopy

from ..load import load


def get_load(states: dict[tuple[int, int], int]) -> int:
    return sum(v for _, v in states.items())


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


def apply_shortcut(
    states: dict[tuple[int, int], int], shortcut: tuple[int, int]
) -> dict[tuple[int, int], int]:
    n1, n2 = shortcut

    for (a, b), dist in states.items():
        short: int = (
            min(
                states[(a, n1)] + states[(b, n2)],
                states[(a, n2)] + states[(b, n1)],
            )
            + 1
        )

        # print(f"short: {shortcut} -> apply({a, b}) -> find({short})")
        if short < dist:
            states[(a, b)] = states[(b, a)] = short

    return states


def setup(
    portals: int, shortcuts: list[tuple[int, int]]
) -> tuple[dict[tuple[int, int], int], int]:  # (n1, n2), min_dist | initial_load
    states: dict[tuple[int, int], int] = {}

    for a in range(portals):
        for b in range(portals):
            initial: int = min(abs(a - b), abs((max(a, b) - portals) - min(a, b)))
            compressed, remaining = divmod(initial, 3)
            initial = compressed + (1 if remaining else 0)

            states[(a + 1, b + 1)] = states[(b + 1, a + 1)] = initial

    initial_load: int = get_load(states)

    # print(*dict(sorted(states.items())).items(), sep="\n")

    for sc in shortcuts:
        states = apply_shortcut(states, sc)

    return states, initial_load


def solve(portals: int, shortcuts: list[tuple[int, int]]) -> int:

    states, initial_load = setup(portals, shortcuts)

    # print(*dict(sorted(states.items())).items(), sep="\n")

    res: int = initial_load

    for start in range(1, (step := portals // 8) + 1):
        positions: set[int] = set()
        while start <= portals:
            positions.add(start)
            start += step

        for a, b, c, d in generate_pairings(list(positions)):
            cpy = deepcopy(states)
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
