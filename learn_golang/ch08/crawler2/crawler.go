package main

import (
	"fmt"
	"log"
	"net/http"
	"os"

	"golang.org/x/net/html"
)

func Extract(url string) ([]string, error) {
	resp, err := http.Get(url)
	if err != nil {
		return nil, err
	}
	if resp.StatusCode != http.StatusOK {
		resp.Body.Close()
		return nil, fmt.Errorf("getting %s: %s", url, resp.Status)
	}

	doc, err := html.Parse(resp.Body)
	resp.Body.Close()
	if err != nil {
		return nil, fmt.Errorf("parsing %s as HTML: %v", url, err)
	}

	var links []string
	visitNode := func(n *html.Node) {
		if n.Type == html.ElementNode && n.Data == "a" {
			for _, a := range n.Attr {
				if a.Key != "href" {
					continue
				}
				link, err := resp.Request.URL.Parse(a.Val)
				if err != nil {
					continue // ignore bad URLs
				}
				links = append(links, link.String())
			}
		}
	}
	forEachNode(doc, visitNode, nil)
	return links, nil
}

// Copied from gopl.io/ch5/outline2.
func forEachNode(n *html.Node, pre, post func(n *html.Node)) {
	if pre != nil {
		pre(n)
	}
	for c := n.FirstChild; c != nil; c = c.NextSibling {
		forEachNode(c, pre, post)
	}
	if post != nil {
		post(n)
	}
}

var tokens = make(chan struct{}, 20)

func crawl(url string) []string {
	fmt.Println(url)

	// Block action when there has been 20 elements in the channel
	tokens <- struct{}{}
	list, err := Extract(url)
	// Wrap the most expensive operation
	<-tokens

	if err != nil {
		log.Print(err)
	}
	return list
}

func main() {

	worklist := make(chan []string)
	seen := make(map[string]bool)
	var n int

	n++
	go func() { worklist <- os.Args[1:] }()

	// Avoid hanging when there is nothing in the channel
	for ; n>0; n-- {
		list := <-worklist
		// Iterate the strings (link) in the slice
		for _, link := range list {
			if !seen[link] {
				seen[link] = true
				n++
				// this is a good way to put a function into goroutine
				go func(link string) {
					worklist <- crawl(link)
				}(link)
			}
		}
	}
}
