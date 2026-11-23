package main

import (
	"fmt"
	load "lotw/quest_1"
)

func calc(x int) int {
	return x*4 + 4
}

func Solve(data []int) int {
	var n int = 1
	var res int = 0
	for _, outpost := range data {
		var r int = calc(n)
		for ; r < outpost; r = calc(n) {
			n++
		}
		res += r - outpost
	}
	return res
}

func main() {
	fmt.Println(Solve(load.From("quest_1/p2/in.txt")))
}
