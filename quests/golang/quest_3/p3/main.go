package main

import (
	"fmt"
	"log"
	quest3 "lotw/quest_3"
	"strconv"
)

func valid(base string, mul string) bool {
	var c int = quest3.ToInt(base, mul)
	n, err := strconv.Atoi(mul)
	if err != nil {
		log.Fatal(err)
	}

	for i := 0; i < n; i++ {
		if quest3.ToInt(base, strconv.Itoa(i)) == c {
			return false
		}
	}
	return true
}

func Solve(data []quest3.Vote) int {
	var res int = 0
	for _, vote := range data {
		if valid(vote.STD, vote.Vote) {
			res += quest3.ToInt(vote.STD, vote.Vote)
		}
	}
	return res
}

func main() {
	fmt.Println(Solve(quest3.Load("quest_3/p3/in.txt")))
}
