from quests.load import EverybodyCodesAPI


def load(part: int) -> list[list[str]]:
    return [list(i) for i in EverybodyCodesAPI().get_input(17)[part].split("\n")]
