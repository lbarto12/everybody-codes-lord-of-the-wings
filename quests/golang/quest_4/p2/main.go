package main

import (
	"fmt"
	quest4 "lotw/quest_4"
	"slices"
)

func Solve(data []quest4.Rank) int {
	var n int = quest4.MaxID(data)
	var times []quest4.TimePart = make([]quest4.TimePart, n)

	for _, rank := range data {
		tp := times[rank.ID-1]
		times[rank.ID-1] = quest4.TimePart{
			Part: tp.Part + 1,
			Time: tp.Time + rank.Time,
		}
	}
	slices.SortFunc(times, func(i quest4.TimePart, j quest4.TimePart) int {
		p := j.Part - i.Part
		if p != 0 {
			return p
		}

		t := i.Time - j.Time
		return t
	})

	var res int = 0
	for place, time := range times {
		res += (place + 1) * time.Time
	}

	return res
}

func main() {
	fmt.Println(Solve(quest4.Load(2)))
}
