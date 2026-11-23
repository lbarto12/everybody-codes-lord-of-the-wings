from quests.python.load import EverybodyCodesAPI


def load(part: int) -> list[list[str]]:
    lines: list[str] = EverybodyCodesAPI().get_input(15)[part].split("\n")
    return [list(i) for i in lines]
