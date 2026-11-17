def load(path: str):
    with open(path) as file:
        return file.read().strip()
