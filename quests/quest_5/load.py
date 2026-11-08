from quests.load import EverybodyCodesAPI


def load(part: int) -> list[list[str]]:
    lines: list[str] = EverybodyCodesAPI().get_input(5)[part].split("\n")
    res: list[list[str]] = [list(i.strip()) for i in lines]

    return res
