package main

import "fmt"

// It is stupid that there is no builtin function to compare to integers?!
// otherwise, the statement becomes overly redunant for an easy task
// z = make([]int, zlen, int(math.Max(float64(2*len(x)), float64(zlen))))
func maxInt(x, y int) int {
	if x > y {
		return x
	} else {
		return y
	}
}

func appendInt(x []int, y int) []int {
	// Use the new slice to point to the unnamed array
	var z []int
	// len(x) is the last element of the slice x
	zlen := len(x) + 1

	if zlen <= cap(x) {
		z = x[:zlen]
	} else {
		// In this case - len(x) == cap(x)
		// For the starting case, len(x) is zero.
		z = make([]int, zlen, maxInt(2*len(x), zlen))
		copy(z, x)
	}
	z[len(x)] = y
	return z
}

func main() {
	var x []int
	for i := 0; i < 10; i++ {
		x = appendInt(x, i)
		fmt.Printf("%d. cap=%d\t%v\n", i, cap(x), x)
	}
}
