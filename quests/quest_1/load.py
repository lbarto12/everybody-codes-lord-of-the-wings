def load(path: str) -> list[int]:
    with open(path) as file:
        return list(map(int, file.read().split(",")))
