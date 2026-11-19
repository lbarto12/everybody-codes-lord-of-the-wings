import re
from typing import cast


def load(path: str):
    with open(path) as file:
        lines: list[str] = [i.strip() for i in file.readlines()]
        res: list[tuple[int, int]] = [
            cast(
                tuple[int, int],
                tuple([int(x) for x in re.findall(r"x=(\d+) y=(\d+)", i)[0]]),
            )
            for i in lines
        ]

        return res


def load_p2(path: str):
    with open(path) as file:
        lines: list[str] = [i.strip() for i in file.readlines()]
        res: list[tuple[int, int, int]] = [
            cast(
                tuple[int, int, int],
                tuple(
                    [int(x) for x in re.findall(r"x=(\d+) y=(\d+) width=(\d+)", i)[0]]
                ),
            )
            for i in lines
        ]

        return res
