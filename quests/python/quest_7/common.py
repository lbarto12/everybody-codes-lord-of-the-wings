from collections import defaultdict
from typing import TypeAlias


InputLine: TypeAlias = tuple[int, int, set[int]]
Clouds: TypeAlias = defaultdict[int, tuple[int, set[int]]]
