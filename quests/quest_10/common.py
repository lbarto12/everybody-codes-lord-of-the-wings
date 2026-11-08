from copy import deepcopy
from typing import TypeAlias

from quests.common import setxy


Ghost: TypeAlias = tuple[int, tuple[int, int], tuple[int, int]]  # pos, vel


def rotate(t: tuple[int, int]) -> tuple[int, int]:
    return -t[1], t[0]


def ghosts(data: list[list[str]]) -> tuple[list[list[str]], list[tuple[Ghost, int]]]:
    board: list[list[str]] = deepcopy(data)
    ghsts: list[tuple[Ghost, int]] = []

    id: int = 0
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
                ghsts.append(((id, (x, y), v), 0))
                id += 1
                setxy(board, (x, y), ".")

    return board, ghsts
