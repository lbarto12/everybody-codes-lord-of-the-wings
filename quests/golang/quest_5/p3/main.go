package main

import (
	"fmt"
	"lotw"
	"lotw/ds"
	quest5 "lotw/quest_5"
)

func Solve(data [][]rune) int {
	data, _ = quest5.SolveP2(data)

	var trees ds.Set[ds.Vec2[int]] = ds.MakeSet([]ds.Vec2[int]{})
	for y, row := range data {
		for x, c := range row {
			var pos ds.Vec2[int] = ds.Vec2[int]{X: x, Y: y}
			if c == '#' && quest5.CanPlaceTree(data, pos) {
				data[y][x] = '@'
				trees.Add(pos)
			}
		}
	}

	for range 2 {
		var check ds.Set[ds.Vec2[int]] = ds.MakeSet([]ds.Vec2[int]{})
		for tile := range trees.Iter() {
			for x, y := range lotw.Adjacent(tile.X, tile.Y) {
				var p ds.Vec2[int] = ds.Vec2[int]{X: x, Y: y}
				if lotw.InBounds(data, p) && ds.Vec2ArrayGet(data, p) == '#' {
					check.Add(p)
				}
			}
		}

		var gen [][]rune = lotw.Deepcopy2D(data)
		var n int = trees.Len()
		for tile := range check.Iter() {
			if quest5.CountAdj(data, tile, "=") == 0 && quest5.CountAdj(data, tile, "@") >= 4 {
				gen[tile.Y][tile.X] = '@'
				trees.Add(tile)
			}
		}
		if trees.Len() == n {
			break
		}

		data = gen
	}

	return trees.Len()
}

func main() {
	ans := Solve(quest5.Load(3))
	fmt.Println(ans)
}
