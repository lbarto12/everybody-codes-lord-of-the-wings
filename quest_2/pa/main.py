from ..load import load


def deduce(data: list[list[tuple[int, int]]]) -> list[list[tuple[int, int]]]:
    res: list[list[tuple[int, int]]] = []
    for row in data:
        tmp: set[tuple[int, int]] = set(row)
        last: int = len(tmp)
        while True:
            new: set[tuple[int, int]] = set()
            for j, a in enumerate(tmp):
                for b in list(tmp)[j + 1 :]:
                    if a[0] == b[1]:
                        new.add((b[0], a[1]))
                    elif a[1] == b[0]:
                        new.add((a[0], b[1]))
            tmp = tmp.union(new)
            if len(tmp) == last:
                break
            last = len(tmp)
        res.append(list(tmp))
    return res


def mx_range(row: list[tuple[int, int]]) -> int:
    mx: int = 0
    for c in row:
        mx = max(mx, *c)
    return mx


def solve(data: list[list[tuple[int, int]]]) -> int:
    data = deduce(data)

    n: int = mx_range(data[0])

    result: int = 0
    for row in data:
        res = [0] * n
        for i in range(1, n + 1):
            res[sum(int(left == i) for left, _ in row)] = i
        result += int("".join(map(str, res)))

    return result


if __name__ == "__main__":
    print("part 1:", solve(load("quest_2/pa/p1.txt")))
    print("part 2:", solve(load("quest_2/pa/p2.txt")))
    print("part 3:", solve(load("quest_2/pa/p3.txt")))
