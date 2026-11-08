import re
from typing import cast

from quests.load import EverybodyCodesAPI
from .common import Plant


def load(part: int) -> list[Plant]:
    lines: list[str] = EverybodyCodesAPI().get_input(9)[part].split("\n")
    result: list[Plant] = []
    for line in lines:
        match = cast(
            tuple[str, str, str],
            re.findall(r"id=(\d+), growth=(\d+), limit=(\d+)", line)[0],
        )
        id, growth, limit = match
        result.append((int(id), int(growth), int(limit)))
    return result
