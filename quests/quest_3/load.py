import re

from quests.load import EverybodyCodesAPI


def load(part: int) -> list[tuple[str, str]]:
    lines: list[str] = EverybodyCodesAPI().get_input(3)[part].split("\n")
    parse = [tuple(re.findall(r"(\w+)-(\d+) (\d+)", line)) for line in lines]
    res: list[tuple[str, str]] = [(i[0][1], i[0][2]) for i in parse]
    return res
