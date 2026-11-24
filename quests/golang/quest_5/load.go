package quest5

import (
	"lotw"
	"strings"
)

func Load(part int) [][]rune {
	var lines []string = strings.Split(lotw.MustEverybodyCodesAPI().MustInput(5)[part], "\n")

	var res [][]rune
	for _, line := range lines {
		res = append(res, []rune(line))
	}

	return res
}
