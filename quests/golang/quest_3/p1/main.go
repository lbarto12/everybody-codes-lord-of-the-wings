package main

import (
	"fmt"
	quest3 "lotw/quest_3"
)

func Solve(data []quest3.Vote) int {
	var res int = 0
	for _, vote := range data {
		res += quest3.ToInt(vote.STD, vote.Vote)
	}
	return res
}

func main() {
	fmt.Println(Solve(quest3.Load(1)))
}
