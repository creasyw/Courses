package main

import (
	"fmt"
	"sort"
)

// prereqs maps computer science courses to their prerequisites.
var prereqs = map[string][]string{
	"algorithms": {"data structures"},
	"calculus":   {"linear algebra"},

	"compilers": {
		"data structures",
		"formal languages",
		"computer organization",
	},

	"data structures":       {"discrete math"},
	"databases":             {"data structures"},
	"discrete math":         {"intro to programming"},
	"formal languages":      {"discrete math"},
	"networks":              {"operating systems"},
	"operating systems":     {"data structures", "computer organization"},
	"programming languages": {"data structures", "computer organization"},
}

func toposort(m map[string][]string) []string {
	var order, keys []string
	// It is used as a set
	seen := make(map[string]bool)
	// Because it is used in the recursive function, it has to be defined before
	// the actual implementation. That is, we cannot use the shortform :=
	var visitAll func(items []string)

	// get it fancy with an anonymous function
	// The input argument (slice) is passed by reference
	visitAll = func(items []string) {
		for _, item := range items {
			// neat way to check if an element is in a set
			if !seen[item] {
				seen[item] = true
				// Check the prerequisites before adding this course to the order
				visitAll(m[item])
				order = append(order, item)
			}
		}
	}
	// IT IS STUPID that there is nothing like map.keys() to get the keys in
	// slice from a map
	for key := range m {
		keys = append(keys, key)
	}

	sort.Strings(keys)
	visitAll(keys)
	return order
}

func main() {
	for i, course := range toposort(prereqs) {
		fmt.Printf("%d:\t\t%s\n", i+1, course)
	}
}
