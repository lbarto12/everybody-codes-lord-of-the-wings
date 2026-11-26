package quest6

import (
	"lotw/ds"

	"github.com/gammazero/deque"
)

func BFS(data map[string][]string, ingredients ds.Set[string], initial []string) int {
	var q deque.Deque[string]
	for _, item := range initial {
		q.PushBack(item)
	}

	for q.Len() != 0 {
		var i string = q.PopFront()
		if ingredients.Contains(i) || i == "NULL" {
			continue
		}
		ingredients.Add(i)

		if _, ok := data[i]; !ok {
			continue
		}

		for _, x := range data[i] {
			q.PushBack(x)
		}
	}

	return ingredients.Len()
}
