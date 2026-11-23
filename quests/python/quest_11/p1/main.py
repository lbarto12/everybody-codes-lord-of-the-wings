from ..load import load


def triangle(n: int) -> int:
    return n * (n + 1) // 2


def crawl(
    portals: int, shortcuts: list[tuple[int, int]]
) -> dict[tuple[int, int], int]:  # (n1, n2), min_dist
    states: dict[tuple[int, int], int] = {
        (a + 1, b + 1): min(abs(a - b), abs((max(a, b) - portals) - min(a, b)))
        for a in range(portals)
        for b in range(portals)
    }

    for n1, n2 in shortcuts:
        for (a, b), dist in states.items():
            short: int = (
                min(
                    (states[(a, n1)] + states[(b, n2)]),
                    states[(a, n2)] + states[(b, n1)],
                )
                + 1
            )

            if short < dist:
                states[(a, b)] = states[(b, a)] = short

    return states


def solve(portals: int, shortcuts: list[tuple[int, int]]) -> int:

    n: int = portals // 2
    initial_load: int = (triangle(n) + triangle(n - 1)) * portals

    states = crawl(portals, shortcuts)

    return initial_load - sum(v for _, v in states.items())


if __name__ == "__main__":
    print(solve(*load(1)))
