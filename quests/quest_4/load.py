import re

from quests.load import EverybodyCodesAPI


def load(part: int) -> list[tuple[int, int, int, int]]:
    lines: list[str] = EverybodyCodesAPI().get_input(4)[part].split("\n")
    res: list[tuple[int, int, int, int]] = []
    for line in lines:
        id, quest, part, time = re.findall(
            r"id=(\d+) quest=(\d+) part=(\d+) time=(\d+)", line
        )[0]
        res.append((int(id), int(quest), int(part), int(time)))
    return res
