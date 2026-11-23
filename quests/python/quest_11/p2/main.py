from copy import deepcopy

from ..load import load
from ..common import setup, get_load, apply_shortcut


def solve(portals: int, shortcuts: list[tuple[int, int]]) -> int:
    states, initial_load = setup(portals, shortcuts)

    res: int = initial_load

    for a in range(portals):
        for b in range(portals):
            cpy = deepcopy(states)
            test: int = get_load(apply_shortcut(cpy, (a + 1, b + 1)))
            if test < res:
                res = test

    return initial_load - res


if __name__ == "__main__":
    print(solve(*load(2)))
