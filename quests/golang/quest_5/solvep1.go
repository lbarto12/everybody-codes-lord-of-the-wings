package quest5

import (
	"lotw"
	"lotw/ds"
)

func SolveP1(data [][]rune) ([][]rune, int) {
	var first ds.Vec2[int] = ds.Vec2[int]{
		X: len(data[0]) / 2,
		Y: len(data) / 2,
	}
	data[first.Y][first.X] = '#'

	var land ds.Set[ds.Vec2[int]] = ds.MakeSet([]ds.Vec2[int]{first})
	var new_land ds.Set[ds.Vec2[int]] = ds.MakeSet([]ds.Vec2[int]{first})

	for true {
		var gen [][]rune = data
		var next_loop ds.Set[ds.Vec2[int]] = ds.MakeSet([]ds.Vec2[int]{})

		for pos := range new_land.Iter() {
			x, y := pos.Unpack()
			if CountAdj(data, pos, "#1") >= 5 || data[y][x] == '#' {
				gen[y][x] = '#'
				land.Add(pos)
				for nx, ny := range lotw.Adjacent(x, y) {
					nxt := ds.Vec2[int]{X: nx, Y: ny}
					if lotw.InBounds(data, nxt) && data[ny][nx] != '#' {
						next_loop.Add(nxt)
					}
				}
			}
		}

		if next_loop.Len() == 0 {
			break
		}
		new_land = next_loop
		data = gen
	}

	var result [][]rune = make([][]rune, len(data))
	for j, row := range data {
		for _, i := range row {
			if i == '#' {
				result[j] = append(result[j], '#')
			} else {
				result[j] = append(result[j], '.')
			}
		}
	}

	return result, land.Len()
}
