package golang

import (
	"bufio"
	"os"
)

func ReadLines(file *os.File) []string {
	var result []string = []string{}
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		result = append(result, scanner.Text())
	}
	file.Close()
	return result
}
