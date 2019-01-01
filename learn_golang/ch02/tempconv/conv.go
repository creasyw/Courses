package tempconv

func CToF(c Celsius) Fehrenheit {
	return Fehrenheit(c*9/5 + 32)
}

func FToC(f Fehrenheit) Celsius {
	return Celsius((f - 32) * 5 / 9)
}
