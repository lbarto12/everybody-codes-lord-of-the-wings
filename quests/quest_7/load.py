from collections import defaultdict
import re
from typing import cast

from quests.load import EverybodyCodesAPI

from .common import InputLine, Clouds


def load(part: int) -> list[InputLine]:
    lines: list[str] = EverybodyCodesAPI().get_input(7)[part].split("\n")
    result: list[tuple[int, int, set[int]]] = []
    for line in lines:
        items: tuple[str, str, str] = cast(
            tuple[str, str, str],
            re.findall(r"id=(\d+), energy=(\d+), connections=(.+)$", line)[0],
        )
        id, energy, connections = items
        result.append((int(id), int(energy), set(map(int, connections.split(",")))))

    return result


def mapify(data: list[InputLine]) -> Clouds:
    result: Clouds = defaultdict(lambda: (0, set()))
    for id, energy, connections in data:
        result[id] = (energy, connections)

    return result
