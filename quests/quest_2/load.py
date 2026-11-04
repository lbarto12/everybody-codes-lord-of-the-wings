import re


def load(path: str = "") -> list[list[tuple[int, int]]]:
    with open(path) as file:
        lines: list[str] = file.readlines()
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
