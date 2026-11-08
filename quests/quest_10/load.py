from quests.load import EverybodyCodesAPI


def load(path: int) -> list[list[str]]:
    lines: list[str] = EverybodyCodesAPI().get_input(10)[path].split("\n")
    return [list(i) for i in lines]
