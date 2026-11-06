from quests.common import getxy, setxy, t_add

from ..common import Cast, rounds

from ..load import load


def solve(data: list[list[str | int]]) -> int:
    w, h = len(data[0]), len(data)

    def in_bounds(p: tuple[int, int]) -> bool:
        return 0 <= p[0] < w and 0 <= p[1] < h

    casts: list[Cast] = rounds(w, h)

    res: int = 0
    warriors: int = 0
    while True:
        for (sx, sy), (ax, ay), (cx, cy) in casts:
            if warriors >= 100_000:
                return res

            while -w <= sx <= w * 2 and -h <= sy <= h * 2:
                shadow: int = 0
                x, y = sx, sy
                while -w <= x <= w * 2 and -h <= y <= h * 2:
                    if in_bounds((x, y)) and type(c := getxy(data, (x, y))) is int:
                        check: int = int(c)
                        if check <= 0:
                            setxy(data, (x, y), c + 1)
                        elif check > shadow:
                            shadow = check
                            res += 1

                            strength: int = c + 1
                            warriors += int((wa := strength >= 10))
                            setxy(data, (x, y), -2 if wa else strength)
                        shadow -= 1

                    x, y = t_add((x, y), (cx, cy))
                sx, sy = t_add((sx, sy), (ax, ay))


if __name__ == "__main__":
    print(solve(load("quests/quest_8/p3/in.txt")))
