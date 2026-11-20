from quests.load import EverybodyCodesAPI


def load(part: int) -> list[list[str]]:
    sections: list[str] = EverybodyCodesAPI().get_input(19)[part].split("\n\n")
    squares: list[str] = [i.strip() for i in sections]
    return [i.split("\n") for i in squares]


def load_p3(part: int) -> list[str]:
    lines: list[str] = EverybodyCodesAPI().get_input(19)[part].split("\n")
    return lines
