import re
from typing import cast

from quests.load import EverybodyCodesAPI


def load(part: int):
    content: str = EverybodyCodesAPI().get_input(11)[part]
    first, last = content.split("\n\n")

    portals: str = cast(str, re.findall(r"portals: (\d+)", first)[0])
    shortcuts: list[tuple[int, int]] = cast(
        list[tuple[int, int]],
        [
            tuple(int(i) for i in x.split(" "))
            for x in filter(lambda g: g, last.split("\n"))
        ],
    )

    return int(portals), shortcuts
