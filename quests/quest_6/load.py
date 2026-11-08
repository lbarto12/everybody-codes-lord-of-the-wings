from quests.load import EverybodyCodesAPI


def load(part: int) -> dict[str, list[str]]:
    lines: list[str] = EverybodyCodesAPI().get_input(6)[part].split("\n")
    result: dict[str, list[str]] = {}
    for line in lines:
        item, ingr = line.split(":")
        result[item] = ingr.split(",")
    return result
