import re

from quests.load import EverybodyCodesAPI


def load(part: int) -> list[list[tuple[int, int]]]:
    lines: list[str] = EverybodyCodesAPI().get_input(2)[part].split("\n")

    res: list[list[list[str]]] = [
        [re.findall(r"(\d+)([><])(\d+)", i) for i in line.strip().split(" ")]
        for line in lines
    ]
    split: list[list[tuple[int, str, int]]] = [
        [(int(x[0][0]), x[0][1], int(x[0][2])) for x in i] for i in res
    ]
    final: list[list[tuple[int, int]]] = []
    for row in split:
        final.append([])
        for eq in row:
            if eq[1] == ">":
                final[-1].append((eq[2], eq[0]))
            else:
                final[-1].append((eq[0], eq[2]))
    return final
