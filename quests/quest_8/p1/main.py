from quests.common import getxy

from ..common import Cast

from ..load import load


def solve(data: list[list[str | int]]) -> int:
    w, h = len(data[0]), len(data)

    def in_bounds(p: tuple[int, int]) -> bool:
        return 0 <= p[0] < w and 0 <= p[1] < h

    dirs: list[Cast] = [((-w, 0), (1, 0), (1, 1))]

    res: int = 0
    for (sx, sy), (ax, ay), (cx, cy) in dirs:
        while -w <= sx < w * 2 and -h <= sy < h * 2:
            shadow: int = 0
            x, y = sx, sy
            while -w <= x < w * 2 and -h <= y < h * 2:
                if in_bounds((x, y)) and type(c := getxy(data, (x, y))) is int:
                    check: int = int(c)
                    if check > shadow:
                        shadow = check
                        res += 1
                    shadow -= 1

                x += cx
                y += cy

            sx += ax
            sy += ay

    return res


if __name__ == "__main__":
    print(solve(load("quests/quest_8/p1/in.txt")))
