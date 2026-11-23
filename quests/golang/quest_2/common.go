package quest2

import (
	"log"
	"lotw/ds"
	"strconv"
)

type Pair struct {
	Left  int
	Right int
}

func deduce(data [][]Pair) [][]Pair {
	res := [][]Pair{}

	for _, row := range data {
		tmp := ds.MakeSet(row).ToSlice()
		last := len(tmp)
		for true {
			_new := ds.MakeSet([]Pair{})
			for j, a := range tmp {
				for _, b := range tmp[j+1:] {
					if a.Left == b.Right {
						_new.Add(Pair{Left: b.Left, Right: a.Right})
					} else if a.Right == b.Left {
						_new.Add(Pair{Left: a.Left, Right: b.Right})
					}
				}
			}
			tmp = ds.MakeSet(tmp).Union(_new).ToSlice()
			if len(tmp) == last {
				break
			}
			last = len(tmp)
		}
		res = append(res, tmp)
	}
	return res
}

func mxrange(row []Pair) int {
	var mx int = 0
	for _, c := range row {
		mx = max(mx, c.Left, c.Right)
	}
	return mx
}

func SolveFrom(data [][]Pair) int {
	data = deduce(data)

	var n int = mxrange(data[0])

	var result int = 0
	for _, row := range data {
		res := make([]int, n)
		for i := 1; i <= n; i++ {
			var idx int = 0
			for _, pair := range row {
				if pair.Left == i {
					idx += 1
				}
			}
			res[idx] = i
		}
		var final string
		for _, c := range res {
			final += strconv.Itoa(c)
		}
		asint, err := strconv.Atoi(final)
		if err != nil {
			log.Fatal("could not parse int")
		}

		result += asint
	}
	return result
}
