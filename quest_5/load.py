def load(path: str) -> list[list[str]]:
    with open(path) as file:
        lines: list[list[str]] = [list(i.strip()) for i in file.readlines()]

        return lines
