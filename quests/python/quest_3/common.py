from typing import cast


def to_int(base: str, mul: str) -> int:
    b, mul, n = base[::-1], mul[::-1], len(mul)
    base = b * (n // len(base) + 1)
    return sum(cast(int, int(m) * int(base[i]) ** i) for i, m in enumerate(mul))
