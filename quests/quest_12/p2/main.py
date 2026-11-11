from quests.quest_12.common import (
    Dims,
    MagmaPatch,
    MagmaSquare,
    dims,
    handle_l,
    missing,
    complete,
    islands,
)
from quests.quest_12.load import load


def solve(data: list[str]) -> int:
    patches: list[MagmaPatch] = islands(data)

    res: int = 0
    for patch in patches:
        total: MagmaSquare = complete(patch)
        total_dims: Dims = dims(total)
        missing_patch: MagmaPatch = missing(patch, total)
        if not missing_patch:
            res += min(*total_dims)
            continue

        missing_sqr: MagmaSquare = complete(missing_patch)
        missing_dims: Dims = dims(missing_sqr)

        res += handle_l(total_dims, missing_dims)

    return res


if __name__ == "__main__":
    print(solve(load(2)))
