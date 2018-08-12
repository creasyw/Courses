package main

import "fmt"

func remove(slice []int, i int) []int {
	copy(slice[i:], slice[i+1:])
	return slice[:len(slice)-i]
}

func main() {
	s := []int{5, 6, 7, 8, 9}
	fmt.Println(remove(s, 3))
}
