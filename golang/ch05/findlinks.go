package main

import (
	"fmt"
	"os"

	"golang.org/x/net/html"
)

func visit(links []string, n *html.Node) []string {
	// Stack the link in the current level into the accumulator
	for _, a := range n.Attr {
		if a.Key == "href" {
			links = append(links, a.Val)
		}
	}
	// Pass the accumulator along to the lower levels
	// It iterates from the FirstChild, so a DFS
	for c := n.FirstChild; c != nil; c = c.NextSibling {
		links = visit(links, c)
	}

	return links
}

func main() {
	doc, err := html.Parse(os.Stdin)
	if err != nil {
		fmt.Fprintf(os.Stderr, "findlink: %v\n", err)
	}

	for _, link := range visit(nil, doc) {
		fmt.Println(link)
	}
}
