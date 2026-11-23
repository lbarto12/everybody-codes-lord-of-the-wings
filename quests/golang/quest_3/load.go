package quest3

import (
	"log"
	"lotw"
	"os"
	"regexp"
)

func Load(path string) []Vote {
	file, err := os.Open(path)
	if err != nil {
		log.Fatal(err)
	}

	var lines []string = lotw.ReadLines(file)

	res := []Vote{}

	pattern := regexp.MustCompile(`ISO-(\d+) (\d+)`)
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
