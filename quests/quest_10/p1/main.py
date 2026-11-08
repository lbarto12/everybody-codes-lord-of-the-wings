from collections import Counter

from quests.common import getxy, t_add

from ..load import load
from ..common import Ghost, ghosts, rotate


def solve(data: list[list[str]]) -> int:

    board, ghsts = ghosts(data)

    collisions: int = 0
    for _ in range(10):
        col: int = 0
        nxt: list[tuple[Ghost, int]] = []
        for (_, pos, vel), _ in ghsts:
            move: tuple[int, int] = t_add(pos, vel)
            if getxy(board, move) == "#":
                col += 1
                move = pos
                vel = rotate(vel)
            nxt.append(((_, move, vel), _))

        counts: Counter[tuple[int, int]] = Counter(i[0][1] for i in nxt)

        for i, ((_, pos, vel), _) in enumerate(nxt):
            if counts[pos] > 1:
                col += 1
                nxt[i] = ((_, pos, rotate(rotate(vel))), _)

        collisions += col
        ghsts = nxt

    return collisions


if __name__ == "__main__":
    ans: int = solve(load(1))
    print(ans)
