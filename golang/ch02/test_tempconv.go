package main

import (
	"fmt"
	"os"
	"strconv"

	// the package has to put into a folder... that's stupid
	"gobook/ch02/tempconv"
)

func main() {
	for _, arg := range os.Args[1:] {
		// Damn! it has to be convert from string to float64, which is the type
		// of both F and C defined at tempconv.go
		t, err := strconv.ParseFloat(arg, 64)
		if err != nil {
			fmt.Fprintf(os.Stderr, "cf: %v\n", err)
			os.Exit(1)
		}
		// it feels handy to not declear the variables until it is used
		f := tempconv.Fehrenheit(t)
		c := tempconv.Celsius(t)
		fmt.Printf("%s = %s, %s = %s", f, tempconv.FToC(f), c, tempconv.CToF(c))
	}
}
