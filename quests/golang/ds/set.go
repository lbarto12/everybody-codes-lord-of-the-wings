// Package ds
package ds

import (
	"iter"
	"maps"
)

type SetInterface[T comparable, S any] interface {
	Add(item T)
	Update(other S)
	UpdateFromSlice(items []T)
	Contains(item T) bool
	Union(other S) S
	Intersection(other S) S
	Iter() iter.Seq[T]
	Iteri() iter.Seq2[int, T]
	ToSlice() []T
	Len() int
}

type Set[T comparable] struct {
	items map[T]struct{}
}

var _ SetInterface[int, Set[int]] = Set[int]{}

func MakeSetFromSlice[T comparable](init []T) Set[T] {
	items := map[T]struct{}{}

	for _, item := range init {
		items[item] = struct{}{}
	}

	set := Set[T]{
		items: items,
	}

	return set
}

func MakeSet[T comparable]() Set[T] {
	return Set[T]{
		items: map[T]struct{}{},
	}
}

func (set Set[T]) Add(item T) {
	set.items[item] = struct{}{}
}

func (set Set[T]) Update(other Set[T]) {
	for x := range other.Iter() {
		set.Add(x)
	}
}

func (set Set[T]) UpdateFromSlice(items []T) {
	for _, x := range items {
		set.Add(x)
	}
}

func (set Set[T]) Contains(item T) bool {
	_, ok := set.items[item]
	return ok
}

func (set Set[T]) Union(other Set[T]) Set[T] {
	cpy := maps.Clone(set.items)

	for k := range other.items {
		cpy[k] = struct{}{}
	}

	return Set[T]{
		items: cpy,
	}
}

func (set Set[T]) Intersection(other Set[T]) Set[T] {
	intersection := map[T]struct{}{}

	for k := range set.items {
		if _, ok := other.items[k]; ok {
			intersection[k] = struct{}{}
		}
	}

	return Set[T]{
		items: intersection,
	}
}

func (set Set[T]) Iter() iter.Seq[T] {
	return func(yield func(T) bool) {
		for k := range set.items {
			if !yield(k) {
				return
			}
		}
	}
}

func (set Set[T]) Iteri() iter.Seq2[int, T] {
	return func(yield func(int, T) bool) {
		i := 0
		for k := range set.items {
			if !yield(i, k) {
				return
			}
			i++
		}
	}
}

func (set Set[T]) ToSlice() []T {
	res := []T{}

	for k := range set.items {
		res = append(res, k)
	}

	return res
}

func (set Set[T]) Len() int {
	return len(set.items)
}
