from collections import defaultdict
from sys import setrecursionlimit
from typing import TypeAlias

from quests.common import DisjointSetUnion, adjacent4, getxy, in_bounds


# weighted, directed graphish thing
Graph: TypeAlias = defaultdict[frozenset[str], int]  # (a, b) : weight


def graphify(data: list[list[str]]) -> tuple[Graph, set[str]]:  # graph, nodes
    setrecursionlimit(1_000_000)
    g: Graph = defaultdict(int)

    seen: set[tuple[int, int]] = set()

    def dfs(c: str, p: tuple[int, int]):
        if p in seen:
            return
        if not (i := in_bounds(data, p)) or getxy(data, p) != c:
            if i:
                o: str = getxy(data, p)
                g[frozenset({c, o})] += 1
            else:
                g[frozenset({"WALL", c})] += 1
            return

        seen.add(p)

        for nxt in adjacent4(p):
            dfs(c, nxt)

    for y, row in enumerate(data):
        for x, c in enumerate(row):
            dfs(c, (x, y))

    return g, {a for a, _ in g}.union({b for _, b in g})


def order_graph(graph: Graph) -> list[tuple[frozenset[str], int]]:
    return list(sorted(graph.items(), key=lambda x: x[1]))


def mst(ordered: list[tuple[frozenset[str], int]], dsu: DisjointSetUnion[str]) -> int:
    res: int = 0

    while len(dsu) > 1:
        (a, b), w = ordered.pop(0)
        if dsu.find(a) == dsu.find(b):
            continue  # already joined
        res += w
        dsu.union(a, b)

    return res
