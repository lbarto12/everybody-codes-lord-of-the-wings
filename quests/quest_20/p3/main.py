from ..load import load
from ..common import to_b11, evaluate, segments, GIVE, GET, SELF


def swap1(i: int, c: str, s: str) -> str:
    return s[:i] + c + s[i + 1 :]


def swap(i: int, c1: str, j: int, c2: str, s: str) -> str:
    return swap1(i, c1, swap1(j, c2, s))


def do_trades(idx: tuple[int, int], give: str, get: str, s: str) -> bool:
    for x in GIVE[give]:
        for y in GET[get]:
            check: str = swap(idx[0], x, idx[1], y, s)
            if evaluate(check):
                return True
    return False


def try_move(s: str) -> int:
    segs: int = segments(s)
    for i, a in enumerate(s):
        for o in SELF.get(a, set()):
            check: str = swap1(i, o, s)
            if evaluate(check):
                return segs
        for j, b in enumerate(s[i + 1 :], i + 1):
            if (a in GIVE and b in GET and do_trades((i, j), a, b, s)) or (
                b in GIVE and a in GET and do_trades((j, i), b, a, s)
            ):
                return segs

    return 0


def solve(data: list[str]) -> str:
    return to_b11(sum(segments(eq) if evaluate(eq) else try_move(eq) for eq in data))


if __name__ == "__main__":
    print(solve(load("quests/quest_20/p3/in.txt")))
