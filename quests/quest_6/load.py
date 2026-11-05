def load(path: str) -> dict[str, list[str]]:
    with open(path) as file:
        lines: list[str] = [i.strip() for i in file.readlines()]

        result: dict[str, list[str]] = {}
        for line in lines:
            item, ingr = line.split(":")
            result[item] = ingr.split(",")
        return result
