from typing import Callable

from quests.common import t_add

from ..common import Pos, Vel, gen_can_move
from ..load import load


def wallhugger(data: list[list[str]], vel: Vel, rotate: Callable[[Pos], Pos]) -> int:
    pos: Pos = (0, 0)
    end: Pos = (len(data[0]) - 1, len(data) - 1)

    can_move: Callable[[Pos], int] = gen_can_move(data)

    trail: int = 1

    while pos != end or can_move(t_add(pos, rotate(vel))):
        if can_move(side := t_add(pos, new_rot := rotate(vel))):
            pos = side
            vel = new_rot
        elif can_move(front := t_add(pos, vel)):
            trail += 1
            pos = front
        elif can_move(
            other_side := t_add(pos, trip_rot := rotate(rotate(rotate(vel))))
        ):
            trail += 2
            pos = other_side
            vel = trip_rot
        else:
            trail += 3
            behind: Pos = t_add(pos, rev_rot := rotate(rotate(vel)))
            vel = rev_rot
            pos = behind

    return trail


def solve(data: list[list[str]]) -> int:
    return min(
        wallhugger(data, (0, 1), lambda x: (-x[1], x[0])),
        wallhugger(data, (1, 0), lambda x: (x[1], -x[0])),
    )


if __name__ == "__main__":
    print(solve(load(3)))
