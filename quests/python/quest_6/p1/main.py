from ..load import load
from ..common import bfs


def solve(data: dict[str, list[str]]) -> int:
    start: list[str] = data["NULL"]
    ingreds: set[str] = set()

    return bfs(data, ingreds, start)


if __name__ == "__main__":
    ans: int = solve(load(1))
    print(ans)
