from copy import deepcopy
from itertools import combinations
from typing import Unpack

from quests.common import DisjointSetUnion

from ..load import load
from ..common import graphify, mst, order_graph


def solve(data: list[list[str]]) -> int:
    graph, nodes = graphify(data)
    ordered: list[tuple[frozenset[str], int]] = order_graph(graph)

    res: int = 100_000  # arbitrary, high
    for c in combinations(nodes, 2):
        if "WALL" in c:
            continue

        ocpy: list[tuple[frozenset[str], int]] = deepcopy(ordered)
        dsu: DisjointSetUnion[str] = DisjointSetUnion(nodes)

        for combo in graph:
            if combo.intersection(c):
                dsu.union(*combo)

        ocpy = [i for i in ocpy if not set(i[0]).intersection(c)]

        res = min(res, mst(ocpy, dsu))

    return res


if __name__ == "__main__":
    print(solve(load(3)))
