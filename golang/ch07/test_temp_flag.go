package main

import (
	"flag"
	"fmt"

	"./tempconv"
)

// Compared with the ch02/test_tempconv.go which use os.Args and
// strconv.parseFloat. Leveraging the usage of flag makes it much easier and
// cleaner to deal with the input variables
func main() {
	var temp = tempconv.CelsiusFlag("temp", 20.0, "the temperature")
	flag.Parse()
	fmt.Println(*temp)
}
