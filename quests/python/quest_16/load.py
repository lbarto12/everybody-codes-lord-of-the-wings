from quests.python.load import EverybodyCodesAPI


def load(part: int):
    return EverybodyCodesAPI().get_input(16)[part].strip()
