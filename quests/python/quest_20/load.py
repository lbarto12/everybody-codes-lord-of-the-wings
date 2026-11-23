from quests.python.load import EverybodyCodesAPI


def load(part: int) -> list[str]:
    lines: list[str] = EverybodyCodesAPI().get_input(20)[part].split("\n")
    return lines
