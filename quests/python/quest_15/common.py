from typing import TypeAlias


Pos: TypeAlias = tuple[int, int]
Vel: TypeAlias = tuple[int, int]
Run: TypeAlias = tuple[Pos, Vel, frozenset[Pos], int]  # _, _, sulfur, dist

Graph: TypeAlias = dict[int, list[tuple[int, int, frozenset[Pos], int]]]
