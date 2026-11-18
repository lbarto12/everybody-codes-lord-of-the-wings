from typing import TypeAlias


Pos: TypeAlias = tuple[int, int]


def load(path: str) -> list[list[str]]:
    with open(path) as file:
        return [list(i.strip()) for i in file.readlines()]
