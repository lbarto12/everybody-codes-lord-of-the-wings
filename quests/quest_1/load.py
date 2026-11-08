from ..load import EverybodyCodesAPI


def load(part: int) -> list[int]:
    data: str = EverybodyCodesAPI().get_input(1)[part]

    return list(map(int, data.split(",")))
