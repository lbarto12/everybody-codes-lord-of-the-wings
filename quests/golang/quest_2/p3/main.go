package main

import (
	"fmt"
	quest2 "lotw/quest_2"
)

func Solve(data [][]quest2.Pair) int {
	return quest2.SolveFrom(data)
}

func main() {
	fmt.Println(Solve(quest2.Load(3)))
}
