from quests.common import getxy, in_bounds, t_add
from quests.quest_12.common import MagmaSquare
from quests.quest_12.load import load_from


def islands(data: list[str]) -> list[MagmaSquare]:
    seen: set[tuple[int, int]] = set()

    def dfs(p: tuple[int, int], best: MagmaSquare) -> MagmaSquare:
        if (
            not in_bounds(list(map(list, data)), p)
            or getxy(data, p) != "#"
            or p in seen
        ):
            return best
        seen.add(p)

        if p < best[0]:
            best = (p, best[1])
        elif p > best[1]:
            best = (best[0], p)

        nxt: list[MagmaSquare] = [
            dfs(t_add(p, (-1, 0)), best),
            dfs(t_add(p, (1, 0)), best),
            dfs(t_add(p, (0, 1)), best),
            dfs(t_add(p, (0, -1)), best),
        ]

        return min(i[0] for i in nxt), max(i[1] for i in nxt)

    res: list[MagmaSquare] = []
    for y, row in enumerate(data):
        for x, c in enumerate(row):
            if c == "#" and (x, y) not in seen:
                res.append(dfs((x, y), ((x, y), (x, y))))

    return res


def solve(data: list[str]) -> int:
    patches: list[MagmaSquare] = islands(data)

    res: int = 0
    for (x1, y1), (x2, y2) in patches:
        res += min(x2 - x1 + 1, y2 - y1 + 1)

    return res


if __name__ == "__main__":
    print(solve(load_from("quests/quest_12/p1/in.txt")))
