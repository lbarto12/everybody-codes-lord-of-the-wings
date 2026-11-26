package quest5

import (
	"lotw"
	"lotw/ds"
	"strings"
)

func CountAdj(data [][]rune, p ds.Vec2[int], cset string) int {
	var res int = 0
	for x, y := range lotw.Adjacent(p.X, p.Y) {
		if lotw.InBounds(data, ds.Vec2[int]{
			X: x,
			Y: y,
		}) && strings.Contains(cset, string(data[y][x])) {
			res++
		}
	}
	return res
}

func AnyWater(data [][]rune, p ds.Vec2[int]) bool {
	for x, y := range lotw.Adjacent(p.X, p.Y) {
		if !lotw.InBounds(data, p) || data[y][x] == '.' {
			return true
		}
	}
	return false
}

func CanPlaceTree(data [][]rune, p ds.Vec2[int]) bool {
	var cancel ds.Set[int] = ds.MakeSetFromSlice([]int{-2, 2})
	for y := -2; y <= 2; y++ {
		for x := -2; x <= 2; x++ {
			if cancel.Contains(x) && cancel.Contains(y) {
				continue
			}
			var pos ds.Vec2[int] = ds.Vec2[int]{
				X: x + p.X,
				Y: y + p.Y,
			}

			if !lotw.InBounds(data, pos) || !strings.Contains("#@", string(ds.Vec2ArrayGet(data, pos))) {
				return false
			}
		}
	}
	return true
}
