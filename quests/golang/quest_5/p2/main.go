package main

import (
	"fmt"
	"lotw"
	"lotw/ds"
	quest5 "lotw/quest_5"
	"slices"
)

func Solve(data [][]rune) ([][]rune, int) {
	data, _ = quest5.SolveP1(data)

	var edge_tiles ds.Set[ds.Vec2[int]] = ds.MakeSet([]ds.Vec2[int]{})
	var initial_beach [][]rune = data
	for y, row := range data {
		for x, c := range row {
			var pos ds.Vec2[int] = ds.Vec2[int]{X: x, Y: y}
			if c == '#' && quest5.AnyWater(data, pos) {
				edge_tiles.Add(pos)
				initial_beach[pos.Y][pos.X] = '='
			}
		}
	}
	data = initial_beach

	var sand ds.Set[ds.Vec2[int]] = ds.MakeSet(slices.Collect(edge_tiles.Iter()))
	for true {
		var check ds.Set[ds.Vec2[int]] = ds.MakeSet([]ds.Vec2[int]{})
		for s := range sand.Iter() {
			for x, y := range lotw.Adjacent(s.X, s.Y) {
				var pos ds.Vec2[int] = ds.Vec2[int]{
					X: x,
					Y: y,
				}
				if lotw.InBounds(data, pos) && ds.Vec2ArrayGet(data, pos) == '#' {
					check.Add(pos)
				}
			}
		}

		var gen [][]rune = data
		var n int = sand.Len()
		for tile := range check.Iter() {
			if quest5.CountAdj(data, tile, "=") >= 5 {
				gen[tile.Y][tile.X] = '='
				sand.Add(tile)
			}
		}
		if sand.Len() == n {
			break
		}

		data = gen
	}

	return data, sand.Len()
}

func main() {
	_, ans := Solve(quest5.Load(2))
	fmt.Println(ans)
}
