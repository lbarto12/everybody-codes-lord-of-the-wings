from collections import defaultdict
import re

from .common import InputLine, Clouds


def load(path: str) -> list[InputLine]:
    with open(path) as file:
        result: list[tuple[int, int, set[int]]] = []
        for line in file.readlines():
            items: tuple[str, str, str] = re.findall(
                r"id=(\d+), energy=(\d+), connections=(.+)$", line
            )[0]
            id, energy, connections = items
            result.append((int(id), int(energy), set(map(int, connections.split(",")))))

        return result


def mapify(data: list[InputLine]) -> Clouds:
    result: Clouds = defaultdict(lambda: (0, set()))
    for id, energy, connections in data:
        result[id] = (energy, connections)

    return result
