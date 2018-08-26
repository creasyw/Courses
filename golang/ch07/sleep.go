package main

import (
	"flag"
	"fmt"
	"time"
)

func main() {
	// THIS IS SO COOL!!!!!
	// It defines both the type of the input and its unit
	// `$ ~ go run sleep.go --period 1m` sleeps 1 minute
	var period = flag.Duration("period", 1*time.Second, "sleep period")
	flag.Parse()
	fmt.Printf("Sleeping for %v seconds...\n", *period)
	time.Sleep(*period)
}
