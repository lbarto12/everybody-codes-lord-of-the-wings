from ..load import load


def pancake_sort(s: str) -> int:
    sm: int = 0
    while len(s) > 1:
        color: str = s[0]
        rest: str = s.lstrip(color)
        parts: list[str] = rest.split(color)
        left, end = parts[:-1], parts[-1]
        lo, hi, flip = 0, len(left) - 1, False
        total: int = sum(map(len, left))
        pieces: list[tuple[str, bool]] = []  # (segment, needs_reverse)
        while lo <= hi:
            f: str
            if flip:
                f = left[hi]
                hi -= 1
            else:
                f = left[lo]
                lo += 1
            if not f:
                continue
            sm += total + (hi - lo + 2)
            total -= len(f)
            pieces.append((f, not flip))
            flip = not flip  # rest of the list is now reversed
        s = "".join(p[::-1] if r else p for p, r in reversed(pieces)) + end
    return sm


def solve(data: str) -> int:
    return pancake_sort(data * 100)


if __name__ == "__main__":
    print(solve(load("quests/quest_16/p3/in.txt")))
