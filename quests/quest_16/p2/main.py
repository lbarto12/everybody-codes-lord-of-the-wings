from ..load import load


def pancake_sort(s: str) -> int:
    i: int = 0
    flips: int = 0
    while i < len(s) - 1:
        while i < len(s) - 1 and s[i] == s[i + 1]:
            i += 1
        r: int = s.rfind(s[i])
        if r == i:
            i += 1
            continue

        flips += len(s[i + 1 : r + 1])
        s = s[: i + 1] + s[i + 1 : r + 1][::-1] + s[r + 1 :]
        print(i, len(s))
    return flips


def solve(data: str) -> int:
    return pancake_sort(data * 10)


if __name__ == "__main__":
    print(solve(load("quests/quest_16/p2/in.txt")))
