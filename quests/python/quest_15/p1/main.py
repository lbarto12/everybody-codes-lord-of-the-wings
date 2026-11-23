import heapq
from itertools import count, pairwise
import sys
from typing import Callable, Hashable

from quests.python.common import adjacent4, getxy, t_add

from ..load import load

Pos = tuple[int, int]
Vel = tuple[int, int]
Run = tuple[Pos, Vel, frozenset[Pos], int]  # _, _, sulfur, dist

Graph = dict[int, list[tuple[int, int, frozenset[Pos], int]]]


def rotate_cw(v: Vel) -> Vel:
    return -v[1], v[0]


def rotate_ccw(v: Vel) -> Vel:
    return v[1], -v[0]


def prepare(
    data: list[list[str]],
) -> tuple[list[list[str]], set[Pos], Pos, Pos]:  # map, sulfurpos, start, end
    start: Pos = (0, 0)
    end: Pos = (0, 0)
    sulfur: set[Pos] = set()

    for y, row in enumerate(data):
        for x, c in enumerate(row):
            if c == "S":
                start = (x, y)
            elif c == "E":
                end = (x, y)
            elif c == "@":
                sulfur.add((x, y))
            else:
                continue
            data[y][x] = "."

    return data, sulfur, start, end


def graphify(data: list[list[str]]) -> tuple[Graph, int, int, frozenset[Pos]]:
    board, sulfur, start, end = prepare(data)
    row = start[1]

    intersections: list[int] = [
        i
        for i in range(1, end[0] - 1)
        if all(getxy(board, x) == "." for x in adjacent4((i, row)))
    ]

    def crawl(
        p: Pos, v: Vel, rotator: Callable[[Vel], Vel]
    ) -> tuple[int, frozenset[Pos], int]:  # len, deposits, exit node
        length = 1  # step off the corridor
        deps: set[Pos] = set()
        while p[1] != row:
            length += 1
            if p in sulfur:
                deps.add(p)
            while getxy(board, x := t_add(p, v)) == "#":
                v = rotator(v)
            p = x
        return length, frozenset(deps), p[0]

    graph: Graph = {}
    eid = count()

    def add_edge(a: int, b: int, length: int, deps: frozenset[Pos]) -> None:
        e = next(eid)
        graph.setdefault(a, []).append((b, length, deps, e))
        graph.setdefault(b, []).append((a, length, deps, e))

    for dy, rotator in ((-1, rotate_cw), (1, rotate_ccw)):
        done: set[int] = set()
        for i in intersections:
            if i in done:
                continue
            length, deps, j = crawl((i, row + dy), (0, dy), rotator)
            done.add(j)
            add_edge(i, j, length, deps)

    for a, b in pairwise([start[0], *intersections, end[0]]):
        deps = frozenset(p for p in sulfur if p[1] == row and a < p[0] <= b)
        add_edge(a, b, b - a, deps)

    return graph, start[0], end[0], frozenset(sulfur)


def shortest[P: Hashable](
    graph: Graph,
    start: int,
    end: int,
    init: P,
    step: Callable[[P, frozenset[Pos]], P],
    finished: Callable[[P], bool],
) -> int:
    tie: count[int] = count()
    best: dict[tuple[int, int, P], int] = {(start, -1, init): 0}
    pq: list[tuple[int, int, int, int, P]] = [(0, next(tie), start, -1, init)]
    while pq:
        dist, _, node, came, prog = heapq.heappop(pq)
        if best[node, came, prog] < dist:
            continue
        if node == end and finished(prog):
            return dist
        for nxt, length, deps, e in graph[node]:
            if e == came:
                continue
            state = (nxt, e, step(prog, deps))
            if dist + length < best.get(state, 1 << 60):
                best[state] = dist + length
                heapq.heappush(pq, (dist + length, next(tie), *state))

    return sys.maxsize


def solve(data: list[list[str]]) -> int:
    graph, s, e, sulfur = graphify(data)
    empty: frozenset[Pos] = frozenset()
    return shortest(graph, s, e, empty, lambda k, d: k | d, lambda k: k == sulfur)


if __name__ == "__main__":
    print(solve(load(1)))
