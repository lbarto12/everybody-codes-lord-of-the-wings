package main

import (
	"fmt"
	quest4 "lotw/quest_4"
	"maps"
	"slices"
	"sort"
)

type QP struct {
	Quest int
	Part  int
}

type IT struct {
	ID   int
	Time int
}

type QI struct {
	Quest int
	ID    int
}

func Solve(data []quest4.Rank) int {
	parts := map[QP][]IT{}

	for _, rank := range data {
		k := QP{
			Quest: rank.Quest,
			Part:  rank.Part,
		}

		parts[k] = append(parts[k], IT{
			ID:   rank.ID,
			Time: rank.Time,
		})
	}

	times := map[QI]int{}
	scores := map[int]int{}

	sorted := slices.Collect(maps.Keys(parts))
	slices.SortFunc(sorted, func(a QP, b QP) int {
		q := a.Quest - b.Quest
		if q != 0 {
			return q
		}

		p := a.Part - b.Part
		return p
	})

	for _, qp := range sorted {
		combo := parts[qp]
		for _, it := range combo {
			times[QI{
				Quest: qp.Quest,
				ID:    it.ID,
			}] += it.Time
		}

		var totals []int
		for _, it := range combo {
			totals = append(totals, times[QI{
				Quest: qp.Quest,
				ID:    it.ID,
			}])
		}
		slices.Sort(totals)

		for _, it := range combo {
			short, _ := slices.BinarySearch(totals, times[QI{
				Quest: qp.Quest,
				ID:    it.ID,
			}])
			scores[it.ID] += max(50*qp.Part-short, 0)
		}
	}

	final := slices.Sorted(maps.Values(scores))

	var res int = 0
	for _, score := range final {
		right := sort.Search(len(final), func(i int) bool {
			return final[i] > score
		})

		res += score * (1 + len(final) - right)
	}

	return res
}

func main() {
	fmt.Println(Solve(quest4.Load(3)))
}
