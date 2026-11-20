def load(path: str) -> list[list[str]]:
    with open(path) as file:
        squares: list[str] = [i.strip() for i in file.read().split("\n\n")]
        return [i.split("\n") for i in squares]


def load_p3(path: str) -> list[str]:
    with open(path) as file:
        return [i.strip() for i in file.readlines()]
