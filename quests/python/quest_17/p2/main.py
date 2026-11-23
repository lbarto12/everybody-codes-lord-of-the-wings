from collections import deque
from typing import Callable

from quests.python.common import adjacent4

from ..load import load
from ..common import Pos, gen_can_move


def solve(data: list[list[str]]) -> int:
    q: deque[tuple[int, Pos]] = deque([(0, (0, 0))])
    seen: set[Pos] = set()
    exposed: int = 0

    can_move: Callable[[Pos], bool] = gen_can_move(data)

    while q:
        dist, pos = q.popleft()

        if pos in seen:
            continue
        seen.add(pos)

        for p in adjacent4(pos):
            if can_move(p):
                q.append((dist + 1, p))
            else:
                exposed += 1

    return exposed


if __name__ == "__main__":
    print(solve(load(2)))
