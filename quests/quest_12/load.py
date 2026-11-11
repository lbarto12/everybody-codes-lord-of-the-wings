from quests.load import EverybodyCodesAPI


def load(part: int):
    lines: list[str] = EverybodyCodesAPI().get_input(12)[part].split("\n")

    return lines


def load_from(path: str):
    with open(path) as file:
        lines: list[str] = file.readlines()
        lines = [i.strip() for i in lines]

        return lines
