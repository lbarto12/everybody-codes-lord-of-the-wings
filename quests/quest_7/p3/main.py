from collections import defaultdict
from copy import deepcopy

from ..load import load, mapify
from ..common import Clouds


def balance(data: Clouds, primary: int, expl_at: int = 1_000_000) -> int:
    graph = deepcopy(data)
    states: dict[int, int] = {k: c for k, (c, _) in data.items()}
    consider: defaultdict[tuple[int, int], int] = defaultdict(int)
    consider[(primary, 10)] = 1

    while consider:
        should_expl: set[int] = set()
        nxt: defaultdict[tuple[int, int], int] = defaultdict(int)
        for (cloud, charge), imp in consider.items():
            if not charge:
                continue

            states[cloud] += charge * imp

            expl: bool = states[cloud] >= expl_at

            for con in graph[cloud][1]:
                nxt[con, charge - 1] += imp
                if expl and cloud not in should_expl:
                    nxt[con, 10] += 1

            if expl:
                should_expl.add(cloud)

        for e in should_expl:
            for _, (_, s) in graph.items():
                if e in s:
                    s.remove(e)
            if e in states:
                del states[e]

            nxt = defaultdict(
                nxt.default_factory, {k: v for k, v in nxt.items() if k[0] != e}
            )

        # print(f"{states=}")

        consider = nxt
        # print(consider)

    # print(states.values())
    return sum(states.values())


def solve(data: Clouds) -> int:

    # print(balance(data, 2, 100))

    for i in data.keys():
        print(f"{i}:", balance(data, i))

    # print([balance(data, i, 100) for i in data.keys()])

    return max([balance(data, i) for i in data.keys()])


if __name__ == "__main__":
    ans: int = solve(mapify(load("quests/quest_7/p3/in.txt")))
    print(ans)
