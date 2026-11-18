from collections import defaultdict, deque
import heapq
import math
import queue
import sys

from quests.common import adjacent4, getxy, in_bounds

from ..load import load

Pos = tuple[int, int]


def solve(data: list[list[str]]) -> int:

    end: Pos = (len(data[0]) - 1, len(data) - 1)

    q: deque[tuple[int, Pos]] = deque([(0, (0, 0))])
    seen: set[Pos] = set()

    while q:
        dist, pos = q.popleft()

        if pos in seen:
            continue
        seen.add(pos)

        if pos == end:
            return dist

        for p in adjacent4(pos):
            if in_bounds(data, p) and getxy(data, p) == "#":
                q.append((dist + 1, p))

    return -1


if __name__ == "__main__":
    print(solve(load("quests/quest_17/p1/in.txt")))
