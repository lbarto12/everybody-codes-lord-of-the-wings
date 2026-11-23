// Package quest2
package quest2

import (
	"log"
	"lotw"
	"strconv"
	"strings"
)

func Load(part int) [][]Pair {
	api, err := lotw.MakeEverybodyCodesAPI()
	if err != nil {
		log.Fatal(err)
	}

	var lines []string = strings.Split(api.MustInput(2)[part], "\n")

	var result [][]Pair = [][]Pair{}
	for _, line := range lines {
		result = append(result, []Pair{})
		n := len(result) - 1

		eqs := strings.Split(line, " ")
		for _, eq := range eqs {

			left, err := strconv.Atoi(string(eq[0]))
			if err != nil {
				log.Fatal("could not parse int")
			}

			right, err := strconv.Atoi(string(eq[2]))
			if err != nil {
				log.Fatal("could not parse int")
			}

			var op byte = eq[1]

			pair := Pair{
				Left:  left,
				Right: right,
			}
			if op == '>' {
				pair = Pair{
					Left:  right,
					Right: left,
				}
			}

			result[n] = append(result[n], pair)
		}
	}

	return result
}
