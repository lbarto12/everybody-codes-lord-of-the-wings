package quest3

import (
	"log"
	"lotw"
	"regexp"
	"strings"
)

func Load(part int) []Vote {
	api, err := lotw.MakeEverybodyCodesAPI()
	if err != nil {
		log.Fatal(err)
	}

	var lines []string = strings.Split(api.MustInput(3)[part], "\n")

	res := []Vote{}

	pattern := regexp.MustCompile(`(\d+) (\d+)`)
	for _, line := range lines {
		for _, match := range pattern.FindAllStringSubmatch(line, -1) {
			std := match[1]
			vote := match[2]

			res = append(res, Vote{
				STD:  std,
				Vote: vote,
			})
		}
	}
	return res
}
