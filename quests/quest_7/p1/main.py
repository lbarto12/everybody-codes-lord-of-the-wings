from collections import deque

from ..load import load, mapify
from ..common import Clouds


def solve(data: Clouds) -> int:

    primary: int = max(data.items(), key=lambda x: len(x[1][1]))[0]

    q: deque[tuple[int, int]] = deque([(primary, 5)])

    while q:
        cloud, sig = q.popleft()

        if not sig:
            continue

        energy, conn = data[cloud]

        data[cloud] = (energy + sig, conn)

        for c in conn:
            q.append((c, sig - 1))

    ans: int = sum([i[0] for i in data.values()])

    return ans


if __name__ == "__main__":
    ans: int = solve(mapify(load("quests/quest_7/p1/in.txt")))
    print(ans)
