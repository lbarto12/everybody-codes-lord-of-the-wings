def get_load(states: dict[tuple[int, int], int]) -> int:
    return sum(v for _, v in states.items())


def apply_shortcut(
    states: dict[tuple[int, int], int], shortcut: tuple[int, int]
) -> dict[tuple[int, int], int]:
    n1, n2 = shortcut

    for (a, b), dist in states.items():
        short: int = (
            min(
                states[(a, n1)] + states[(b, n2)],
                states[(a, n2)] + states[(b, n1)],
            )
            + 1
        )

        # print(f"short: {shortcut} -> apply({a, b}) -> find({short})")
        if short < dist:
            states[(a, b)] = states[(b, a)] = short

    return states


def setup(
    portals: int, shortcuts: list[tuple[int, int]]
) -> tuple[dict[tuple[int, int], int], int]:  # (n1, n2), min_dist | initial_load
    states: dict[tuple[int, int], int] = {}

    for a in range(portals):
        for b in range(portals):
            initial: int = min(abs(a - b), abs((max(a, b) - portals) - min(a, b)))
            compressed, remaining = divmod(initial, 3)
            initial = compressed + (1 if remaining else 0)

            states[(a + 1, b + 1)] = states[(b + 1, a + 1)] = initial

    initial_load: int = get_load(states)

    for sc in shortcuts:
        states = apply_shortcut(states, sc)

    return states, initial_load
