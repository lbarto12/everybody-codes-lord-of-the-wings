// Package quest_1
package quest_1

import (
	"log"
	"lotw"
	"strconv"
	"strings"
)

func Load(part int) []int {
	api, err := lotw.MakeEverybodyCodesAPI()
	if err != nil {
		log.Fatal(err)
	}

	var content string = strings.Trim(api.MustInput(1)[part], "\n")
	var split []string = strings.Split(content, ",")

	res := make([]int, len(split))
	for i, n := range split {
		if res[i], err = strconv.Atoi(n); err != nil {
			log.Fatalf("failed to parse int %s\n", n)
		}
	}

	return res
}
