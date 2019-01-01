package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"strings"
)

func main() {
	counts := make(map[string]int)
	for _, filename := range os.Args[1:] {
		// the ReadFile returns a byte array to the data
		data, err := ioutil.ReadFile(filename)
		if err != nil {
			// Output to the stderr in system log
			fmt.FPrintf(os.Stderr, "Dup3 %v\n", err)
			continue
		}
		for _, line := range strings.Split(string(data), "\n") {
			counts[line]++
		}
	}
	for content, count := range counts {
		if count > 1 {
			fmt.Println("%d\t%s\n", count, content)
		}
	}
}
