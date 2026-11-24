package lotw

import (
	"cmp"
	"slices"
)

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

type Vec2[T cmp.Ordered] struct {
	X T
	Y T
}

func (v Vec2[T]) Add(other Vec2[T]) Vec2[T] {
	return Vec2[T]{
		X: v.X + other.X,
		Y: v.Y + other.Y,
	}
}

func (v Vec2[T]) Unpack() (T, T) {
	return v.X, v.Y
}
