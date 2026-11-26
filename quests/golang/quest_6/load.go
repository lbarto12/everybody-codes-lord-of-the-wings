// Package quest6
package quest6

import (
	"log"
	"lotw"
	"strings"
)

func Load(part int) map[string][]string {
	api, err := lotw.MakeEverybodyCodesAPI()
	if err != nil {
		log.Fatal(err)
	}

	var lines []string = strings.Split(api.MustInput(6)[part], "\n")
	result := map[string][]string{}

	for _, line := range lines {
		var sp []string = strings.Split(line, ":")
		item, ingr := sp[0], sp[1]
		result[item] = strings.Split(ingr, ",")
	}

	return result
}
