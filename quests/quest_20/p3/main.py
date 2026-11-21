from collections import defaultdict
from itertools import combinations

from ..load import load

SEG: dict[str, int] = {
    "0": 6,
    "1": 2,
    "2": 5,
    "3": 5,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 3,
    "8": 7,
    "9": 6,
    "+": 2,
    "-": 1,
    "=": 2,
    "A": 6,
    " ": 0,
}

GIVE: dict[str, set[str]] = {
    "6": {"5"},
    "7": {"1"},
    "8": {"6", "9", "0", "A"},
    "9": {"3", "5"},
    "+": {"-"},
}
GET: defaultdict[str, set[str]] = defaultdict(set)
for k, v in GIVE.items():
    for i in v:
        GET[i].add(k)
print(GET)

SELF: dict[str, set[str]] = {
    "0": {"9", "6", "A"},
    "2": {"3"},
    "3": {"2", "5"},
    "5": {"3"},
    "6": {"9", "A", "0"},
    "9": {"6", "A", "0"},
    "A": {"6", "9", "0"},
}

# si: defaultdict[int, set[str]] = defaultdict(set)
# for k, v in SEG.items():
#     si[v].add(k)
#
# print(si)


def to_b11(n: int) -> str:
    if n == 0:
        return "0"

    digits = "0123456789A"
    sign: str = "-" if n < 0 else ""
    n = abs(n)

    res: list[str] = []
    while n > 0:
        n, rem = divmod(n, 11)
        res.append(digits[rem])

    return sign + "".join(reversed(res))


def b11_sub(s: str) -> str:
    blocks: list[str] = s.split(" ")
    for i, b in enumerate(blocks):
        if b in {"+", "-", "="}:
            continue
        blocks[i] = str(int(b, 11))

    return " ".join(blocks)


def swap(i: int, c1: str, j: int, c2: str, s: str) -> str:
    mutate: list[str] = list(s)
    mutate[i] = c1
    mutate[j] = c2
    return "".join(mutate)


def swap1(i: int, c: str, s: str) -> str:
    mutate: list[str] = list(s)
    mutate[i] = c
    return "".join(mutate)


def try_move(s: str) -> int | None:
    print("trying", s)
    for i, a in enumerate(s):
        if a in SELF:
            for o in SELF[a]:
                check: str = swap1(i, o, s)
                print(check)
                if eval(b11_sub(check).replace("=", "==")):
                    print("FOUND!", check)
                    return sum(SEG[g] for g in s)
        for j, b in enumerate(s[i + 1 :], i + 1):
            # print(a, b)
            if a in GIVE and b in GET:
                print(f"give({a=}) | get({b=})")
                for x in GIVE[a]:
                    for y in GET[b]:
                        check2: str = swap(i, x, j, y, s)
                        print(check2)
                        if eval(b11_sub(check2).replace("=", "==")):
                            print("FOUND!")
                            return sum(SEG[g] for g in s)
            if b in GIVE and a in GET:
                print(f"give({b=}) | get({a=})")
                for x in GET[a]:
                    for y in GIVE[b]:
                        check3: str = swap(i, x, j, y, s)
                        print(check3)
                        if eval(b11_sub(check3).replace("=", "==")):
                            print("FOUND!")
                            return sum(SEG[g] for g in s)

    return None


def solve(data: list[str]) -> str:
    print(len(data))
    res: int = 0
    for eq in data:
        if eval(b11_sub(eq).replace("=", "==")):
            res += sum(SEG[i] for i in eq)
        elif c := try_move(eq):
            res += c

    return to_b11(res)


if __name__ == "__main__":
    print(solve(load("quests/quest_20/p3/in.txt")))
