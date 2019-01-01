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
	// It has the required method =Set= by the interface =flag= so that we can
	// then feed the &f into the =flag.CommandLine.Var=
	f := celsiusFlag{value}
	// The actual horsepower to use the CommandLine from flag to parse the f
	// But it still feels counter-intuitive to have the =&f= feeding into the
	// =flag= within the package of tempconv but still have to call the
	// =flag.Parse= from the main package so that it can be correectly decoded
	flag.CommandLine.Var(&f, name, usage)
	return &f.Celsius
}
