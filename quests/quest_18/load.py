import re
from typing import cast

from quests.load import EverybodyCodesAPI


def load_p1() -> list[tuple[int, int]]:
    lines: list[str] = EverybodyCodesAPI().get_input(18)[1].split("\n")
    res: list[tuple[int, int]] = [
        cast(
            tuple[int, int],
            tuple(
                [int(x) for x in cast(list[str], re.findall(r"x=(\d+) y=(\d+)", i)[0])]
            ),
        )
        for i in lines
    ]

    return res


def load(part: int) -> list[tuple[int, int, int]]:
    lines: list[str] = EverybodyCodesAPI().get_input(18)[part].split("\n")
    res: list[tuple[int, int, int]] = [
        cast(
            tuple[int, int, int],
            tuple(
                [
                    int(x)
                    for x in cast(
                        list[str], re.findall(r"x=(\d+) y=(\d+) width=(\d+)", i)[0]
                    )
                ]
            ),
        )
        for i in lines
    ]

    return res
