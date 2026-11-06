from typing import TypeAlias


Cast: TypeAlias = tuple[
    tuple[int, int], tuple[int, int], tuple[int, int]
]  # start, axis, dir


def rounds(w: int, h: int) -> list[Cast]:
    return [
        ((-w, 0), (1, 0), (1, 1)),
        ((w * 2, 0), (-1, 0), (-1, 1)),
        ((w * 2, 0), (0, 1), (-1, 0)),
        ((w * 2, h), (-1, 0), (-1, -1)),
        ((-w, h), (1, 0), (1, -1)),
        ((-w, 0), (0, 1), (1, 0)),
    ]
