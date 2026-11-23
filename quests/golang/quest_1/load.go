// Package quest_1
package quest_1

import (
	"log"
	"os"
	"strconv"
	"strings"
)

func Load(path string) []int {
	bytes, err := os.ReadFile(path)
	if err != nil {
		log.Fatal(err)
	}

	var content string = string(bytes)
	content = strings.Trim(content, "\n")
	var split []string = strings.Split(content, ",")

	res := make([]int, len(split))
	for i, n := range split {
		if res[i], err = strconv.Atoi(n); err != nil {
			log.Fatalf("failed to parse int %s\n", n)
		}
	}

	return res
}
