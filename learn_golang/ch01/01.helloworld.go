package main

import (
	"fmt"
	"os"
	"strings"
)

func echo() {
	var s, sep string
	for _, arg := range os.Args[1:] {
		s += sep + arg
		sep = " "
	}
	fmt.Println(s)
}

func main() {
	fmt.Println(strings.Join(os.Args[1:], "++"))
}
