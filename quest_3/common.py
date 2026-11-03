def to_int(base: str, mul: str) -> int:
    res: int = 0

    b, mul, n = base[::-1], mul[::-1], len(mul)
    base = b
    while len(base) < n:
        base += b
    for i, m in enumerate(mul):
        res += int(m) * (int(base[i]) ** i)

    return res
