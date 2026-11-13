from quests.load import EverybodyCodesAPI


def load(part: int) -> list[list[str]]:
    lines: list[str] = EverybodyCodesAPI().get_input(14)[part].split("\n")
    return [list(i) for i in lines]
