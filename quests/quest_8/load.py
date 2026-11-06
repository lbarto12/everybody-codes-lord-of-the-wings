# def load(path: str) -> list[list[int]]:
#     with open(path) as file:
#         lines: list[str] = [i.strip() for i in file.readlines()]
#
#         side_len: int = sum(i.isdigit() for i in lines[0])
#         w, h = len(lines[0]), len(lines)
#
#         result: list[list[int]] = []
#
#         for x in range(-side_len - 1, w, 2):
#             start: tuple[int, int] = (x, 0)
#             result.append([])
#             for off in range(h):
#                 check: tuple[int, int] = (start[0] + off, start[1] + off)
#                 if (
#                     0 <= check[0] < w
#                     and 0 <= check[1] < h
#                     and (c := getxy(lines, check)).isdigit()
#                 ):
#                     result[-1].append(int(c))
#
#         return list(filter(lambda x: x, result))


def load(path: str) -> list[list[str | int]]:
    with open(path) as file:
        result: list[list[str | int]] = []

        for line in [i.strip() for i in file.readlines()]:
            result.append(list[str | int]())
            for c in line:
                result[-1].append(int(c) if c.isdigit() else c)

    return result
