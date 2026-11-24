package lotw

import (
	"cmp"
	"iter"
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

func Adjacent(x int, y int) iter.Seq2[int, int] {
	return func(yield func(int, int) bool) {
		for i := -1; i <= 1; i++ {
			for j := -1; j <= 1; j++ {
				if !yield(x+j, y+i) {
					return
				}
			}
		}
	}
}

func Adjacent4(x int, y int) iter.Seq2[int, int] {
	return func(yield func(int, int) bool) {
		for _, off := range []Vec2[int]{
			{X: -1, Y: 0},
			{X: 1, Y: 0},
			{X: 0, Y: -1},
			{X: 0, Y: 1},
		} {
			if !yield(x+off.X, y+off.Y) {
				return
			}
		}
	}
}
