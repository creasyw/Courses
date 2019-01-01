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


func crawl(url string) []string {
	fmt.Println(url)
	list, err := Extract(url)

	if err != nil {
		log.Print(err)
	}
	return list
}

func main() {

	worklist := make(chan []string)
	unseenLinks := make(chan string)

	go func() { worklist <- os.Args[1:] }()

	// Spaw 20 goroutine for processing the URL
	for i := 0; i < 20; i++ {
		go func() {
			// This is a fucking block action -- the link would wait until
			// something coming out of the channe
			for link := range unseenLinks {
				foundLinks := crawl(link)
				go func { worklist <- foundLinks }()
			}
		}()
	}

	seen := make(map[string]bool)
	// Because of the blocking nature of the channel, this is similar to
	// crawler1 which would hang if there is nothing in the worklist channel
	for links := range worklist {
		// Iterate the strings (link) in the slice
		for _, link := range list {
			if !seen[link] {
				seen[link] = true
				unseenLinks <- link
			}
		}
	}
}


/*
Things I've learned in these three examples -

- The easiest way to processing items is to use =range channel= to wait (hang) the goroutine
- The single capacity channel can be used to do the synchronization
- The buffered channel can be used to limit the number of goroutines
- To avoid deadlock, it'd better to make each channel do single directional communication

*/
