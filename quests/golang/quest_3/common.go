// Package quest3
package quest3

import (
	"log"
	"lotw"
	"strconv"
	"strings"
)

type Vote struct {
	STD  string
	Vote string
}

func ToInt(base string, mul string) int {
	var b string = lotw.Streverse(base)
	mul = lotw.Streverse(mul)
	var n int = len(mul)
	base = strings.Repeat(b, (n/len(base) + 1))

	var res int = 0
	for i, m := range mul {
		bInt, err := strconv.Atoi(string(base[i]))
		if err != nil {
			log.Fatal(err)
		}
		bInt = lotw.Ipow(bInt, i)

		mInt, err := strconv.Atoi(string(m))

		res += mInt * bInt
	}
	return res
}
