package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	counts := make(map[string]int)
	files := os.Args[1:]
	if len(files) == 0 {
		// Here is interesting - the os.Stdin returns the os.File.
		// Stdin, Stdout, and Stderr are open Files pointing to the standard
		// input, standard output, and standard error file descriptors.
		// var (
		// 	Stdin  = NewFile(uintptr(syscall.Stdin), "/dev/stdin")
		// 	Stdout = NewFile(uintptr(syscall.Stdout), "/dev/stdout")
		// 	Stderr = NewFile(uintptr(syscall.Stderr), "/dev/stderr")
		// )
		countLines(os.Stdin, counts)
	} else {
		for _, arg := range files {
			f, err := os.Open(arg)
			if err != nil {
				fmt.Fprintf(os.Stderr, "dup: %v\n", err)
				continue
			}
			countLines(f, counts)
			f.Close()
		}
	}
	for line, n := range counts {
		if n > 1 {
			fmt.Printf("%d\t%s\n", n, line)
		}
	}
}

/*
A map is a reference to the data structure created by make. When a map is passed
to a function, the function receives a copy of the reference, so any changes the
called function makes to the underlying data structure will be visible through
the caller’s map reference too.
*/
func countLines(f *os.File, counts map[string]int) {
	input := bufio.NewScanner(f)
	// The Scan is "streaming" the content of a file into the program
	for input.Scan() {
		counts[input.Text()]++
	}
}
