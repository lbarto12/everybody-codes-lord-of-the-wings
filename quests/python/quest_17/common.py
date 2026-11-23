from typing import Callable, TypeAlias

from quests.python.common import getxy, in_bounds


Pos: TypeAlias = tuple[int, int]
Vel: TypeAlias = tuple[int, int]


def gen_can_move(data: list[list[str]]) -> Callable[[Pos], bool]:
    def _wrapper(p: Pos) -> bool:
        return in_bounds(data, p) and getxy(data, p) == "#"

    return _wrapper
