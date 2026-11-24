package quest4

type Rank struct {
	ID    int
	Quest int
	Part  int
	Time  int
}

type TimePart struct {
	Part int
	Time int
}

func MaxID(data []Rank) int {
	var mx int = 0
	for _, rank := range data {
		mx = max(mx, rank.ID)
	}
	return mx
}
