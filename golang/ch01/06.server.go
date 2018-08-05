package main

import (
	"fmt"
	"log"
	"net/http"
	"sync"
)

var mu sync.Mutex
var count int

func main() {
	// The sequence of the handler functions does not matter
	http.HandleFunc("/", handler)
	http.HandleFunc("/count", counter)
	// ListenAndServe always returns an error, since it only returns when an
	// unexpected error occurs. In order to log that error we wrap the function
	// call with log.Fatal.
	log.Fatal(http.ListenAndServe("localhost:8000", nil))
}

// This handler handles everything but the _count_ page
// Another interesting thing is for a URL localhost:8000/this/is/a/long/path
// the handler is called for every slice of the path -- the count adds 5 after
// show up the entire path, but the previous paths are overwritten by the final
// longest path. This might not be the desirable behavior
func handler(w http.ResponseWriter, r *http.Request) {
	// This mutex works for avoiding the conflicting check and adding especially
	// for the long path -- avoid the race condition since every incoming
	// request runs in a separate goroutine
	mu.Lock()
	count++
	mu.Unlock()
	// Write the formatted string to the designated writer
	// an interesting thing is that the `w` should be an io.Writer
	// while the input paramter says it is a http.ResponseWriter
	fmt.Fprintf(w, "URL.Path = %q\n\n", r.URL.Path)
	header_details(w, r)
}

// Print the details of a HTTP request
func header_details(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "%s %s %s\n", r.Method, r.URL, r.Proto)
	for k, v := range r.Header {
		fmt.Fprintf(w, "Header[%q] = %q\n", k, v)
	}
	fmt.Fprintf(w, "Host = %q\n", r.Host)
	fmt.Fprintf(w, "RemoteAddr = %q\n", r.RemoteAddr)
	// ParseForm parses the raw query from the URL and updates r.Form.
	// It is also a compact way to check the error
	if err := r.ParseForm(); err != nil {
		log.Print(err)
	}
	for k, v := range r.Form {
		fmt.Fprintf(w, "URL values - Form[%q] = %q\n", k, v)
	}
}

// Count the echoes and show in the `/count` page
func counter(w http.ResponseWriter, r *http.Request) {
	mu.Lock()
	fmt.Fprintf(w, "Count %d\n", count)
	mu.Unlock()
}
