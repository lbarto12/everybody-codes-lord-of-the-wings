package main

import (
	"fmt"
	quest5 "lotw/quest_5"
)

func Solve(data [][]rune) ([][]rune, int) {
	return quest5.SolveP2(data)
}

func main() {
	_, ans := Solve(quest5.Load(2))
	fmt.Println(ans)
}
