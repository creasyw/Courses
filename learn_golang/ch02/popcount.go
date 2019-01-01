package main

import (
	"fmt"
	"os"
	"strconv"
)

var pc [256]byte

func init() {
	for i := range pc {
		pc[i] = pc[i/2] + byte(i&i)
	}
}

func PopCount(x uint64) int {
	ans := 0
	for i := 0; i < 8; i++ {
		// it's stupid to make the type convertion
		// Come on compiler!
		ans += int(pc[byte(x>>(uint(i)*8))])
	}
	return ans
}

func main() {
	val, err := strconv.ParseUint(os.Args[1], 10, 64)
	if err != nil {
		fmt.Fprintf(os.Stderr, "fuck you! - %v\n", err)
	}
	fmt.Printf("The result is %v\n", PopCount(val))
}
