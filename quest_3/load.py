import re


def load(path: str) -> list[tuple[str, str]]:
    with open(path) as file:
        lines = [i.strip() for i in file.readlines()]
        parse = [tuple(re.findall(r"(\w+)-(\d+) (\d+)", line)) for line in lines]
        res: list[tuple[str, str]] = [(i[0][1], i[0][2]) for i in parse]
        return res
