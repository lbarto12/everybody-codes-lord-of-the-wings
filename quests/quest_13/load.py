from quests.load import EverybodyCodesAPI

from .common import Dir, Hand


def load(part: int) -> list[list[Hand]]:  # hands, total rotational value
    res: list[list[Hand]] = []
    lines: str = EverybodyCodesAPI().get_input(13)[part]
    clocks: list[list[str]] = [i.strip().split("\n") for i in lines.split("\n\n")]
    for clock in clocks:
        _hands, _direction, _current, _move = clock

        hands: list[int] = list(map(int, _hands[5:].split(":")))
        direction: list[str] = [i.strip() for i in _direction[9:].split(":")]
        current: list[int] = list(map(int, _current[7:].split(":")))
        move: list[int] = list(map(int, _move[4:].split(":")))

        res.append([])
        for i, hand in enumerate(hands):
            res[-1].append(
                Hand(
                    id=i,
                    step=hand,  # (total_ticks // hand),
                    direction=Dir(direction[i]),
                    position=current[i],
                    seconds=move[i],
                )
            )

    return res
