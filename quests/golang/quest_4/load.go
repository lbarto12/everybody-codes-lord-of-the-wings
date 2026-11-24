// Package quest4
package quest4

import (
	"log"
	"lotw"
	"regexp"
	"strconv"
	"strings"
)

func Load(part int) []Rank {
	api, err := lotw.MakeEverybodyCodesAPI()
	if err != nil {
		log.Fatal(err)
	}

	var lines []string = strings.Split(api.MustInput(4)[part], "\n")

	pattern := regexp.MustCompile(`id=(\d+) quest=(\d+) part=(\d+) time=(\d+)`)

	var result []Rank
	for _, line := range lines {
		for _, match := range pattern.FindAllStringSubmatch(line, -1) {
			id, err := strconv.Atoi(match[1])
			if err != nil {
				log.Fatal(err)
			}

			quest, err := strconv.Atoi(match[2])
			if err != nil {
				log.Fatal(err)
			}

			part, err := strconv.Atoi(match[3])
			if err != nil {
				log.Fatal(err)
			}

			time, err := strconv.Atoi(match[4])
			if err != nil {
				log.Fatal(err)
			}

			result = append(result, Rank{
				ID:    id,
				Quest: quest,
				Part:  part,
				Time:  time,
			})
		}
	}
	return result
}
