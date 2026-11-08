from collections import Counter

from quests.common import getxy, t_add

from ..load import load
from ..common import Ghost, ghosts, rotate


def solve(data: list[list[str]]) -> int:

    board, ghsts = ghosts(data)

    rounds: int = 0
    while ghsts:
        nxt: list[tuple[Ghost, int]] = []
        for (_, pos, vel), col in ghsts:
            move: tuple[int, int] = t_add(pos, vel)
            if getxy(board, move) == "#":
                col += 1
                move = pos
                vel = rotate(vel)
            nxt.append(((_, move, vel), col))

        nxt = list(filter(lambda x: x[1] < 10_000, nxt))

        counts: Counter[tuple[int, int]] = Counter(i[0][1] for i in nxt)

        for i, ((_, pos, vel), col) in enumerate(nxt):
            if counts[pos] > 1:
                nxt[i] = ((_, pos, rotate(rotate(vel))), col + 1)

        nxt = list(filter(lambda x: x[1] < 10_000, nxt))

        rounds += 1
        ghsts = nxt

    return rounds


if __name__ == "__main__":
    ans: int = solve(load(2))
    print(ans)
