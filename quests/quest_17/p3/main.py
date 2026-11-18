from time import sleep
from typing import Callable

from quests.common import getxy, in_bounds, t_add


from ..load import load

Pos = tuple[int, int]


def wallhugger(
    data: list[list[str]], vel: tuple[int, int], rotate: Callable[[Pos], Pos]
) -> int:
    pos: Pos = (0, 0)
    end: Pos = (len(data[0]) - 1, len(data) - 1)

    trail: int = 0

    def can_move(to: Pos) -> bool:
        return in_bounds(data, to) and getxy(data, to) == "#"

    while pos != end or can_move(t_add(pos, rotate(vel))):
        side: Pos = t_add(pos, new_rot := rotate(vel))

        front: Pos = t_add(pos, vel)
        other_side: Pos = t_add(pos, trip_rot := rotate(rotate(rotate(vel))))
        behind: Pos = t_add(pos, rev_rot := rotate(rotate(vel)))

        if can_move(side):
            pos = side
            vel = new_rot
        elif can_move(front):
            trail += 1
            pos = front
        elif can_move(other_side):
            trail += 2
            pos = other_side
            vel = trip_rot
        else:
            trail += 3
            vel = rev_rot
            pos = behind

    return trail + 1


def solve(data: list[list[str]]) -> int:
    return min(
        wallhugger(data, (0, 1), lambda x: (-x[1], x[0])),
        wallhugger(data, (1, 0), lambda x: (x[1], -x[0])),
    )


if __name__ == "__main__":
    print(solve(load("quests/quest_17/p3/in.txt")))
