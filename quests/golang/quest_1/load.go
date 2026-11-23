// Package quest_1
package quest_1

import (
	"fmt"
	"log"
	"lotw"
	"os"
	"strconv"
	"strings"
)

func Load(path string) []int {
	api, err := lotw.MakeEverybodyCodesAPI()
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println(api.MustInput(1))

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
