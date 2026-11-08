from quests.load import EverybodyCodesAPI


def load(part: int) -> list[list[str | int]]:
    lines: list[str] = EverybodyCodesAPI().get_input(8)[part].split("\n")
    result: list[list[str | int]] = []

    for line in lines:
        result.append(list[str | int]())
        for c in line:
            result[-1].append(int(c) if c.isdigit() else c)

    return result
