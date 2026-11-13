from quests.common import DisjointSetUnion


from ..load import load
from ..common import graphify, mst, order_graph


def solve(data: list[list[str]]) -> int:
    graph, nodes = graphify(data)
    ordered: list[tuple[frozenset[str], int]] = order_graph(graph)

    return mst(ordered, DisjointSetUnion[str](nodes))


if __name__ == "__main__":
    print(solve(load(2)))
