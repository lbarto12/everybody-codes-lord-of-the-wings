def load(path: str):
    with open(path) as file:
        return [i.strip() for i in file.readlines()]
