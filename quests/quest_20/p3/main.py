from ..load import load
from ..common import to_b11, evaluate, segments, GIVE, GET, SELF


def swap1(i: int, c: str, s: str) -> str:
    return s[:i] + c + s[i + 1 :]


def swap2(i: int, c1: str, j: int, c2: str, s: str) -> str:
    return swap1(i, c1, swap1(j, c2, s))


def try_move(s: str) -> int:
    segs: int = segments(s)
    for i, a in enumerate(s):
        for o in SELF.get(a, set()):
            if evaluate(swap1(i, o, s)):
                return segs

        for x in GIVE.get(a, ()):
            for j, b in enumerate(s):
                if j != i:
                    for y in GET.get(b, ()):
                        if evaluate(swap2(i, x, j, y, s)):
                            return segments(s)

    return 0


def solve(data: list[str]) -> str:
    return to_b11(sum(segments(eq) if evaluate(eq) else try_move(eq) for eq in data))


if __name__ == "__main__":
    print(solve(load(3)))
