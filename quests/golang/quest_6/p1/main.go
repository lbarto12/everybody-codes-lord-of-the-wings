package main

import (
	"fmt"
	"lotw/ds"
	quest6 "lotw/quest_6"
)

func Solve(data map[string][]string) int {
	var start []string = data["NULL"]
	var ingredients ds.Set[string] = ds.MakeSet[string]()

	return quest6.BFS(data, ingredients, start)
}

func main() {
	fmt.Println(Solve(quest6.Load(1)))
}
