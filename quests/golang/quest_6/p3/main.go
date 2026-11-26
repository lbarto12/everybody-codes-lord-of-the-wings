package main

import (
	"fmt"
	"lotw/ds"
	quest6 "lotw/quest_6"
	"strings"

	"github.com/gammazero/deque"
)

func Solve(data map[string][]string) int {
	flipped := map[string][]string{}
	for item, ingredients := range data {
		for _, ingredient := range ingredients {
			flipped[ingredient] = append(flipped[ingredient], item)
		}
	}

	var entries []string
	for i := range flipped {
		if strings.HasPrefix(i, "NULL") {
			entries = append(entries, i)
		}
	}

	chains := map[string]ds.Set[string]{}

	for _, item := range entries {
		var start []string = flipped[item]
		var q deque.Deque[string]
		for _, i := range start {
			q.PushBack(i)
		}

		for q.Len() != 0 {
			var i string = q.PopFront()
			if chains[item].Contains(i) || strings.HasPrefix(i, "NULL") {
				continue
			}
			if _, ok := chains[item]; !ok {
				chains[item] = ds.MakeSet([]string{})
			}
			chains[item].Add(i)

			if _, ok := flipped[i]; !ok {
				continue
			}

			for _, x := range flipped[i] {
				q.PushBack(x)
			}
		}
	}

	var doubles ds.Set[string] = ds.MakeSet([]string{})
	for item_1, i_1 := range chains {
		for item_2, i_2 := range chains {
			if item_1 == item_2 {
				continue
			}

			for x := range i_1.Intersection(i_2).Iter() {
				doubles.Add(x)
			}
		}
	}

	return doubles.Len()
}

func main() {
	fmt.Println(Solve(quest6.Load(3)))
}
