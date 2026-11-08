from collections import Counter

from quests.common import getxy, t_add

from ..load import load
from ..common import Ghost, rotate, ghosts


def to_state(
    data: list[tuple[Ghost, int]], round: int
) -> tuple[tuple[Ghost, ...], tuple[int, dict[int, int]]]:  # round, { id: collisions }
    key: tuple[Ghost, ...] = tuple(i[0] for i in data)
    counts: dict[int, int] = {x[0][0]: x[1] for x in data}
    return key, (round, counts)


def cycle_until_next_death(
    data: list[tuple[Ghost, int]],
    start_counts: dict[int, int],
    cycle_len: int,
    round: int,
    limit: int,
) -> tuple[list[tuple[Ghost, int]], int]:
    deltas: dict[int, int] = {g[0]: c - start_counts[g[0]] for g, c in data}
    k: int = min((limit - 1 - c) // deltas[g[0]] for g, c in data if deltas[g[0]] > 0)
    new_data: list[tuple[Ghost, int]] = [(g, c + k * deltas[g[0]]) for g, c in data]
    return new_data, round + k * cycle_len


def solve(data: list[list[str]]) -> int:

    board, ghsts = ghosts(data)

    _k, _v = to_state(ghsts, 0)
    states: dict[tuple[Ghost, ...], tuple[int, dict[int, int]]] = {_k: _v}

    limit: int = 1000000000000

    rounds: int = 0
    while ghsts:
        # print(rounds)
        nxt: list[tuple[Ghost, int]] = []
        for (id, pos, vel), col in ghsts:
            move: tuple[int, int] = t_add(pos, vel)
            if getxy(board, move) == "#":
                col += 1
                move = pos
                vel = rotate(vel)
            nxt.append(((id, move, vel), col))

        nxt = list(filter(lambda x: x[1] < limit, nxt))

        counts: Counter[tuple[int, int]] = Counter(i[0][1] for i in nxt)

        for i, ((id, pos, vel), col) in enumerate(nxt):
            if counts[pos] > 1:
                nxt[i] = ((id, pos, rotate(rotate(vel))), col + 1)

        nxt = list(filter(lambda x: x[1] < limit, nxt))

        rounds += 1
        ghsts = nxt

        state, (_, cnts) = to_state(ghsts, rounds)
        if state in states:  # cycle!
            r, start_counts = states[state]
            ghsts, rounds = cycle_until_next_death(
                ghsts, start_counts, rounds - r, rounds, limit
            )
            states = {}
        else:
            states.update({state: (rounds, cnts)})

    return rounds


if __name__ == "__main__":
    ans: int = solve(load("quests/quest_10/p3/in.txt"))
    print(ans)
