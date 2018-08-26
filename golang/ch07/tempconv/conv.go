package tempconv

import (
	"flag"
	"fmt"
)

func CToF(c Celsius) Fehrenheit {
	return Fehrenheit(c*9/5 + 32)
}

func FToC(f Fehrenheit) Celsius {
	return Celsius((f - 32) * 5 / 9)
}

/*
package flag
// Value is the interface to the value stored in a flag.
type Value interface {
	String() string
	Set(string) error
}
*/

// celsiusFlag satisfies the flag.Value interface.
type celsiusFlag struct{ Celsius }

func (f *celsiusFlag) Set(s string) error {
	var unit string
	var value float64
	fmt.Sscanf(s, "%f%s", &value, &unit)

	switch unit {
	case "C":
		f.Celsius = Celsius(value)
		return nil
	case "F":
		f.Celsius = FToC(Fehrenheit(value))
		return nil
	}
	return fmt.Errorf("invalid temperature %q", s)
}

func CelsiusFlag(name string, value Celsius, usage string) *Celsius {
	// To contruct the celsiusFlag use {} rather than ()
	f := celsiusFlag{value}
	// The actual horsepower to use the CommandLine from flag to parse the f
	flag.CommandLine.Var(&f, name, usage)
	return &f.Celsius
}
