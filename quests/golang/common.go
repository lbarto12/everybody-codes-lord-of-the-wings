package lotw

import "slices"

func Streverse(s string) string {
	r := []rune(s)
	slices.Reverse(r)
	return string(r)
}

func Ipow(x int, e int) int {
	var r int = 1
	for ; e > 0; e-- {
		r *= x
	}
	return r
}
