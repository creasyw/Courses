package main

import (
	"fmt"
	// the package has to put into a folder... that's stupid
	"gobook/ch02/tempconv"
)

func main() {
	fmt.Printf("The absolute zero is %v\n", tempconv.AbsoluteZeroC)
	fmt.Printf("It equals to %v\n", tempconv.CToF(tempconv.AbsoluteZeroC))
}
