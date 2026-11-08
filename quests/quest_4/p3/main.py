import bisect
from collections import defaultdict

from ..load import load


def solve(data: list[tuple[int, int, int, int]]) -> int:
    parts: dict[tuple[int, int], list[tuple[int, int]]] = defaultdict(list)
    for id, quest, part, time in data:
        parts[(quest, part)].append((id, time))

    times: dict[tuple[int, int], int] = defaultdict(int)
    scores: dict[int, int] = defaultdict(int)

    for quest, part in sorted(parts):
        combo: list[tuple[int, int]] = parts[(quest, part)]
        for id, time in combo:
            times[(quest, id)] += time

        totals: list[int] = list(sorted(times[(quest, id)] for id, _ in combo))
        for id, _ in combo:
            short: int = bisect.bisect_left(totals, times[(quest, id)])
            scores[id] += max(50 * part - short, 0)

    final: list[int] = sorted(scores.values())
    return sum(
        score * (1 + len(final) - bisect.bisect_right(final, score)) for score in final
    )


if __name__ == "__main__":
    print(solve(load(3)))
