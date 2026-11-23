package main

import (
	"fmt"
	load "lotw/quest_1"
	"math"
)

func Solve(data []int) int {
	var n int = 1
	var res int = 0
	for _, outpost := range data {
		var r int = int(math.Pow(float64(n), 2))
		for ; r < outpost; r = int(math.Pow(float64(n), 2)) {
			n++
		}
		res += r - outpost
	}
	return res
}

func main() {
	fmt.Println(Solve(load.From("quest_1/p1/in.txt")))
}
