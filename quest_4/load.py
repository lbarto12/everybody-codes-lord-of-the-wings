import re


def load(path: str) -> list[tuple[int, int, int, int]]:
    with open(path) as file:
        res: list[tuple[int, int, int, int]] = []
        for line in file.readlines():
            id, quest, part, time = re.findall(
                r"id=(\d+) quest=(\d+) part=(\d+) time=(\d+)", line
            )[0]
            res.append((int(id), int(quest), int(part), int(time)))
        return res
