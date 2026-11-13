from quests.common import adjacent4, getxy, in_bounds

from ..load import load


def solve(data: list[list[str]]) -> int:
    seen: set[tuple[int, int]] = set()

    def dfs(c: str, p: tuple[int, int]) -> int:
        if p in seen:
            return 0
        if not in_bounds(data, p) or getxy(data, p) != c:
            return 1

        seen.add(p)

        return sum(dfs(c, nxt) for nxt in adjacent4(p))

    res: int = 0
    for y, row in enumerate(data):
        for x, c in enumerate(row):
            res += dfs(c, (x, y))

    return res


if __name__ == "__main__":
    print(solve(load(1)))
