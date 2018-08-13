package main

import (
	"fmt"
	"io"
	"io/ioutil"
	"net/http"
	"os"
	"time"
)

func main() {
	start := time.Now()
	ch := make(chan string)

	for _, url := range os.Args[1:] {
		// The Goroutine starts here _asynchronously_
		go fetch(url, ch)
	}
	for range os.Args[1:] {
		fmt.Println(<-ch)
	}
	fmt.Printf("%.2fs elapsed\n", time.Since(start).Seconds())
}

func fetch(url string, ch chan<- string) {
	start := time.Now()
	resp, err := http.Get(url)
	if err != nil {
		// Sprint returns a string that goes to the buffer (channel)
		ch <- fmt.Sprint(err)
		return
	}

	// Print out everything
	b, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		ch <- fmt.Sprint("while reading %s: %v", url, err)
		return
	}
	fmt.Printf("%s\n", b)

	nbytes, err := io.Copy(ioutil.Discard, resp.Body)
	// it is a good practice to close the response first before checking if
	// there is any content
	resp.Body.Close()
	if err != nil {
		ch <- fmt.Sprint("while reading %s: %v", url, err)
		return
	}
	secs := time.Since(start).Seconds()
	// %7d means the integer takes 7 spaces - a good way to format the output
	ch <- fmt.Sprintf("%.2fs %7d %s", secs, nbytes, url)
}
