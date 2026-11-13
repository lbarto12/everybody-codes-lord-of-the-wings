from functools import cache

from ..load import load, mapify
from ..common import Clouds


def solve(data: Clouds) -> int:
    primary: int = max(data.items(), key=lambda x: len(x[1][1]))[0]

    @cache
    def dfs(cloud: int, energy: int) -> int:
        return (
            1
            if energy == 1
            else energy + sum(dfs(i, energy - 1) for i in data[cloud][1])
        )

    return sum([i[0] for i in data.values()]) + dfs(primary, 10)


if __name__ == "__main__":
    ans: int = solve(mapify(load(2)))
    print(ans)
