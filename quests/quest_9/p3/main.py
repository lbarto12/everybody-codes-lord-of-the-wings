from quests.quest_9.common import Plant

from ..load import load

from math import comb


# Brainstorming
# All preexisting branches fork every n // 2 + 1 steps
# The right branches split every n steps
# every split creates a new right branch, adding 1 leaf, and restarting the left branch's loop
#
# Maybe, maintain a mod window? no numbers too large in input
# Is there a cyclical pattern to the exponentiation?
#
# n = 5, 1 leaf, 1 branch
# 5 seconds -> 5
# fork, 2 leaves, 3 branches
# 3 seconds -> 8
# left forks, stem forks, 4 leaves, 7 branches
#
# Maybe something to do with the total number of segments in the plant?
# if we maintain a simple count of branches, can we do something as a result
# of knowing that?
#
#
# Oh my god, linalg? no.
#
# Combinatorics of some, stupid kind.
#
# I can smell a logarithm in here man, new leaves appear at least every n // 2 + 1 steps, right?
# it just doesn't fit perfectly...
#
# What about a scheduler? we know that some split at A, causes another split at (A + n // 2 + 1) and at (n - 1)
# The spatial complexity of a memo is going to be absolutely stupid, so that's out
# what about only storing the next splits? no, same issue
#
# ok we know that one chain will go all the way to the max height in exactly g seconds, because
# that is the chain that contains exatly the original stem
#
# That also implies that there is a leaf right beside it that took all the same routes except the final branch
#
# Ok ok, this is going to be t = summation of some a * short + b * long step, but all the intersections to get there matter.
# so maybe we start by finding all combos of a and b such that t < limit, and go through them one by one,
# smallest to largest. We know that for some (a, b), time(a, b) occured at n + a * ((n + 1) / 2) + b * (n - 1)
# so time(a, b) < limit for all a, b in Z+ occured
#
# We also know the maximum length will occur on the original stem, as it repeatedly splits every (n + 1) / 2
# Thus, our upper bound for (a, b) is a? (am I being stupid?)
#
# Ok, cominations, here I fucking come you lil shit


def counts(a: int, b: int) -> int:
    return comb(a + b, a) * (2**a)


def time(growth: int, a: int, b: int) -> int:
    return growth + a * ((growth + 1) // 2) + b * (growth - 1)


def combos(growth: int, limit: int) -> list[tuple[int, int]]:
    res: list[tuple[int, int]] = []

    bound: int = limit.bit_length()

    for a in range(bound):
        for b in range(bound):
            res.append((a, b))

    return list(sorted(res, key=lambda x: time(growth, *x)))


def solve(data: list[Plant]) -> int:

    res: int = 0
    for id, growth, limit in data:
        if limit <= 1:
            res += 1
            continue

        t: int = 0
        leaves: int = 1
        combs = combos(growth, limit)

        while combs:
            c = combs.pop(0)
            consider: set[tuple[int, int]] = {c}
            while combs and time(growth, *combs[0]) == time(growth, *c):
                consider.add(combs.pop(0))
            if not consider:
                break

            t = time(growth, *c)

            leaves_this_layer: int = 0
            for a, b in consider:
                leaves_this_layer += counts(a, b)

            if (nxt := leaves + leaves_this_layer) >= limit:
                break

            leaves = nxt

        res += t

    return res


if __name__ == "__main__":
    ans: int = solve(load("quests/quest_9/p3/in.txt"))
    print(ans)
