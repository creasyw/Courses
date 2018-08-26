package tempconv

import (
	"fmt"
)

type Celsius float64
type Fehrenheit float64

const (
	AbsoluteZeroC Celsius = -273.15
	FreezingC     Celsius = 0
	BoilingC      Celsius = 100
)

// These are the __str__ functions in Python objects
func (c Celsius) String() string {
	return fmt.Sprintf("%g C", c)
}

func (f Fehrenheit) String() string {
	return fmt.Sprintf("%g F", f)
}
