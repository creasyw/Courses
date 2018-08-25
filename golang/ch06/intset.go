package main

import (
	"bytes"
	"fmt"
)

// IntSet is a list of unit64.
// Every element in the list has 64 bits to hash
// Every bit in an element might be either 0 (nonexist) or 1 (exist)
// As a result, every element in the IntSet takes 2**64 - 1 numbers
type IntSet struct {
	words []uint64
}

// Use a simple hash function to decide if the word is in the set
func (s *IntSet) Has(x int) bool {
	word, bit := x/64, uint(x%64)
	return word < len(s.words) && s.words[word]&(1<<bit) != 0
}

func (s *IntSet) Add(x int) {
	word, bit := x/64, uint(x%64)
	for word >= len(s.words) {
		// The "append" seems counter-intuitive in a "number" point of view
		// But it actually increases the index of s.words, so it carrries the
		// hashed number to the "next word" associated with the index
		s.words = append(s.words, 0)
	}
	s.words[word] |= 1 << bit
}

func (s *IntSet) UnionWith(t *IntSet) {
	for i, tword := range t.words {
		if i < len(s.words) {
			s.words[i] |= tword
		} else {
			s.words = append(s.words, tword)
		}
	}
}

// Write the Set - Writing everything in a buffer and finally get the entire
// string from the buffer
func (s *IntSet) String() string {
	var buf bytes.Buffer
	buf.WriteByte('{')
	// We use the index of a word for its hashing, so have to get the index to
	// restore the actual word
	for i, word := range s.words {
		if word == 0 {
			continue
		}
		for j := 0; j < 64; j++ {
			// The 1<<uint64 is the tricky part - note that the element in the
			// integer rather than a bit array. So we have to use the word AND that
			// j bit to decide if we have that bit in the set
			if word&(1<<uint(j)) != 0 {
				if buf.Len() > len("{") {
					buf.WriteByte(' ')
				}
				// The word in the accumulated value in the i-th bucket. To
				// restore the value, we only need the index of the word and the
				// index of the bit array that is marked as 1 from the value of the
				// word
				fmt.Fprintf(&buf, "%d", 64*i+j)
			}
		}
	}
	buf.WriteByte('}')
	return buf.String()
}

func main() {
	var x, y IntSet
	x.Add(1)
	x.Add(144)
	x.Add(9)
	fmt.Println(x.String())

	y.Add(9)
	y.Add(42)
	fmt.Println(y.String())

	x.UnionWith(&y)
	fmt.Println(x.String())

	fmt.Printf("9 is in x? - %v\n123 is in x? - %v\n", x.Has(9), x.Has(123))
}
