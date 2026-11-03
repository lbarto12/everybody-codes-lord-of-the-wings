from ..load import load


def solve(data: list[tuple[int, int, int, int]]) -> int:
    data.sort(key=lambda x: (x[1], x[2], x[-1]))
    # print(*data, sep="\n")
    n: int = max([i[0] for i in data])
    q: int = max(i[1] for i in data)
    setup: list[list[tuple[int, int, int]]] = [list() for _ in range(q)]
    for id, quest, part, time in data:
        setup[quest - 1].append((id, part, time))

    quests: list[list[list[tuple[int, int]]]] = [list() for _ in range(q)]
    for i, quest in enumerate(setup):
        p: int = max([x[1] for x in quest])
        quests[i] = [list() for _ in range(p)]
        for id, part, time in quest:
            quests[i][part - 1].append((id, time))

    counts: list[list[int]] = [
        [i * 50 for i in range(1, max(i[2] for i in data) + 1)] for _ in range(q)
    ]
    print(counts)
    scores: list[int] = [0] * n
    print(scores)
    for q, quest in enumerate(quests):
        times: list[int] = [0] * n
        for p, part in enumerate(quest):
            print(times)
            fixed = list(sorted(part, key=lambda x: times[x[0] - 1] + x[1]))

            print(f"{fixed=}")
            prev: int = -1
            skip: int = 1
            for i, (id, time) in enumerate(fixed):
                print(
                    f"quest={q + 1}, part={p + 1}, {id=}, time=({times[id - 1]} + {time})"
                )
                time = times[id - 1] + time

                if prev != -1:
                    if time == times[prev - 1]:
                        skip += 1
                    else:
                        counts[q][p] -= skip
                        skip = 1

                print(f"score={scores[id - 1]} + {max(counts[q][p], 0)} = ", end="")
                scores[id - 1] += max(counts[q][p], 0)
                print(f"{scores[id - 1]}")

                times[id - 1] = time
                prev = id
            print(list(sorted(scores, reverse=True)))
            print()

    prev: int = -1
    skip: int = 1
    rank: int = 1
    final: list[int] = sorted(scores, reverse=True)
    result: int = 0

    for i, score in enumerate(final):
        if prev != -1:
            if score == final[i - 1]:
                skip += 1
            else:
                rank += skip
                skip = 1

        print(f"{rank}. {score}")
        result += rank * score

        prev = score

    return result


if __name__ == "__main__":
    print(solve(load("quest_4/p3/in.txt")))
