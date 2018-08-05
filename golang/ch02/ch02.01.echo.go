package main

import (
	// This library for command line parsing is soooo cool!
	// It even has "-help" built in
	"flag"
	"fmt"
	"strings"
)

// Defines a bool flag with specified name, default value, and usage string.
var n = flag.Bool("n", false, "omit trailing newline")
var sep = flag.String("s", " ", "separator")

func main() {
	// All commandline parsing is only one line!
	flag.Parse()
	// Note that both `n` and `sep` are references
	fmt.Print(strings.Join(flag.Args(), *sep))
	if !*n {
		fmt.Println()
	}
}
