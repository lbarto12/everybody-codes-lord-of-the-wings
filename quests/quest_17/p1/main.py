from collections import deque
from typing import Callable

from quests.common import adjacent4

from ..load import load
from ..common import Pos, gen_can_move


def solve(data: list[list[str]]) -> int:
    end: Pos = (len(data[0]) - 1, len(data) - 1)

    q: deque[tuple[int, Pos]] = deque([(0, (0, 0))])
    seen: set[Pos] = set()

    can_move: Callable[[Pos], int] = gen_can_move(data)

    while q:
        dist, pos = q.popleft()

        if pos in seen:
            continue
        seen.add(pos)

        if pos == end:
            return dist

        for p in adjacent4(pos):
            if can_move(p):
                q.append((dist + 1, p))

    return -1


if __name__ == "__main__":
    print(solve(load(1)))
