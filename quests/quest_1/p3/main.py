from ..load import load


def calc(x: int) -> int:
    return x**2 - 1


def solve(data: list[int]) -> int:
    n: int = 3
    res: int = 0
    for outpost in data:
        while (r := calc(n)) < outpost:
            n += 2
        res += r - outpost

    return res


if __name__ == "__main__":
    print(solve(load(3)))
