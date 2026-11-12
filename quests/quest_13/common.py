from enum import StrEnum
from fractions import Fraction
from itertools import combinations
import math
from typing import TypedDict


class Dir(StrEnum):
    CW = "CW"
    CCW = "CCW"


class Hand(TypedDict):
    id: int
    step: int
    direction: Dir
    position: int
    seconds: int


def total_crossings(a: Fraction, b: Fraction) -> int:
    return (
        math.floor(b) - math.floor(a)
        if b > a
        else math.ceil(a) - math.ceil(b)
        if a > b
        else 0
    )


def speed(hand: Hand) -> Fraction:
    d: int = 1 if hand["direction"] == Dir.CW else -1
    return Fraction(d, hand["step"])


def compute_2_hands(a: Hand, b: Hand) -> int:
    g: Fraction = Fraction(a["position"], a["step"]) - Fraction(
        b["position"], b["step"]
    )
    t: int = 0
    res: int = 0

    for end in sorted({a["seconds"], b["seconds"]}):
        va, vb = (
            speed(a) if t < a["seconds"] else 0,
            speed(b) if t < b["seconds"] else 0,
        )
        nxt: Fraction = g + (end - t) * (va - vb)
        res += total_crossings(g, nxt)
        g, t = nxt, end

    return res


def solve_part(data: list[list[Hand]]) -> int:
    res: int = 0
    for handset in data:
        for h1, h2 in combinations(handset, 2):
            res += compute_2_hands(h1, h2)

    return res
