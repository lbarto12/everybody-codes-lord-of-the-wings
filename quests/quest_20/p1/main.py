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
    " ": 0,
}


def solve(data: list[str]) -> int:
    res: int = 0
    for eq in data:
        if eval(eq.replace("=", "==")):
            res += sum(SEG[i] for i in eq)

    return res


if __name__ == "__main__":
    print(solve(load("quests/quest_20/p1/in.txt")))
