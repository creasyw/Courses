package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	// Simply use the map as a set
	seen := make(map[string]bool)
	// Nice to scan the input and process each line
	input := bufio.NewScanner(os.Stdin)
	for input.Scan() {
		line := input.Text()
		if !seen[line] {
			seen[line] = true
			fmt.Println(line)
		}
	}
	// Nice to deal with the error later
	if err := input.Err(); err != nil {
		fmt.Fprintf(os.Stderr, "dedup: %v\n", err)
		os.Exit(1)
	}
}
