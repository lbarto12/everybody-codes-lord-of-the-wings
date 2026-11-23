package main

import (
	"fmt"
	load "lotw/quest_1"
)

func calc(x int) int {
	return x*x - 1
}

func Solve(data []int) int {
	var n int = 3
	var res int = 0

	var r int = calc(n)
	for _, outpost := range data {
		for ; r < outpost; r = calc(n) {
			n += 2
		}
		res += r - outpost
	}

	return res
}

func main() {
	fmt.Println(Solve(load.From("quest_1/p3/in.txt")))
}
