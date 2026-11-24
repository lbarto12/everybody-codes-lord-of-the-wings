package quest5

import (
	"lotw"
	"strings"
)

func CountAdj(data [][]rune, p lotw.Vec2[int], cset string) int {
	var res int = 0
	for x, y := range lotw.Adjacent(p.X, p.Y) {
		if lotw.InBounds(data, lotw.Vec2[int]{
			X: x,
			Y: y,
		}) && strings.Contains(cset, string(data[y][x])) {
			res++
		}
	}
	return res
}
