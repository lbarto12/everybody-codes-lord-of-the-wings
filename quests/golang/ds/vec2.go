package ds

import "cmp"

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

func Vec2ArrayGet[T any](data [][]T, v Vec2[int]) T {
	return data[v.Y][v.X]
}
