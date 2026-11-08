from collections import defaultdict
from copy import deepcopy

from ..load import load, mapify
from ..common import Clouds


def balance(data: Clouds, primary: int, expl_at: int = 1_000_000) -> int:
    graph: Clouds = deepcopy(data)
    states: dict[int, int] = {k: c for k, (c, _) in data.items()}
    consider: defaultdict[tuple[int, int], int] = defaultdict(int)
    consider[(primary, 10)] = 1

    while consider:
        exploding: set[int] = set()
        nxt: defaultdict[tuple[int, int], int] = defaultdict(int)
        for (cloud, charge), imp in consider.items():
            if not charge:
                continue

            states[cloud] += charge * imp

            expl: bool = states[cloud] >= expl_at

            for con in graph[cloud][1]:
                nxt[con, charge - 1] += imp
                if expl and cloud not in exploding:
                    nxt[con, 10] += 1

            if expl:
                exploding.add(cloud)

        for cloud in exploding:
            for _, (_, s) in graph.items():
                if cloud in s:
                    s.remove(cloud)
            if cloud in states:
                del states[cloud]

            nxt = defaultdict(
                nxt.default_factory, {k: v for k, v in nxt.items() if k[0] != cloud}
            )

        consider = nxt

    return sum(states.values())


def solve(data: Clouds) -> int:
    return max([balance(data, i) for i in data.keys()])


if __name__ == "__main__":
    ans: int = solve(mapify(load(3)))
    print(ans)
