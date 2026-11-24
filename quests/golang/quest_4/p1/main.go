package main

import (
	"fmt"
	quest4 "lotw/quest_4"
	"slices"
)

func Solve(data []quest4.Rank) int {
	var n int = quest4.MaxID(data)
	var times []int = make([]int, n)

	for _, rank := range data {
		times[rank.ID-1] += rank.Time
	}
	slices.Sort(times)

	var res int = 0
	for place, time := range times {
		res += (place + 1) * time
	}

	return res
}

func main() {
	fmt.Println(Solve(quest4.Load(1)))
}
