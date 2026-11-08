from collections import Counter
from copy import deepcopy

from quests.common import getxy, setxy, t_add

from ..load import load
from ..common import Ghost


def rotate(t: tuple[int, int]) -> tuple[int, int]:
    return -t[1], t[0]


def ghosts(data: list[list[str]]) -> tuple[list[list[str]], list[Ghost]]:
    board: list[list[str]] = deepcopy(data)
    ghsts: list[Ghost] = []

    for y, row in enumerate(board):
        for x, c in enumerate(row):
            if c in "><v^":
                match c:
                    case "<":
                        v = (-1, 0)
                    case ">":
                        v = (1, 0)
                    case "v":
                        v = (0, 1)
                    case "^":
                        v = (0, -1)
                    case _:
                        v = (0, 0)
                ghsts.append(((x, y), v))
                setxy(board, (x, y), ".")

    return board, ghsts


def solve(data: list[list[str]]) -> int:

    board, ghsts = ghosts(data)

    collisions: int = 0
    for _ in range(10):
        col: int = 0
        nxt: list[Ghost] = []
        for pos, vel in ghsts:
            move: tuple[int, int] = t_add(pos, vel)
            if getxy(board, move) == "#":
                col += 1
                move = pos
                vel = rotate(vel)
            nxt.append((move, vel))

        counts: Counter[tuple[int, int]] = Counter(i[0] for i in nxt)

        for i, (pos, vel) in enumerate(nxt):
            if counts[pos] > 1:
                col += 1
                nxt[i] = (pos, rotate(rotate(vel)))

        collisions += col
        ghsts = nxt

    return collisions


if __name__ == "__main__":
    ans: int = solve(load("quests/quest_10/p1/in.txt"))
    print(ans)
