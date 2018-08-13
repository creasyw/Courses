package main

import "fmt"

func main() {
	f := func(x int) int {
		return x * x
	}

	fmt.Println("2^2 =", f(2))
	fmt.Println("3^3 =", f(3))
	fmt.Println("4^4 =", f(4))
	fmt.Println("5^5 =", f(5))
}
