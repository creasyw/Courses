package main

import (
	"bufio"
	"fmt"
	"log"
	"net"
)

// It is actually not a bad idea to make global in a package. It shares the
// states among the functions, reduces the complexity of the API, and does not
// pollute the name space outside of the package

// Using a channel for each client
// It is great! - the channel can hold a string and get all of the properties of
// a channel, in which most importantly it is blocked by nature. Then, we can
// also pass it through the entering and leaving messages below
type client chan<- string

var (
	// These are three kinds of information that each connected client would
	// handle
	entering = make(chan client)
	leaving  = make(chan client)
	messages = make(chan string)
)

// THIS IS SOOOOO COOL!!!!
// The main routine runs a TCP server to listen on the given port
// It spawns one routine dispatch the messages, and each connection is handled
// by a goroutine via handleConn.
func main() {
	listener, err := net.Listen("tcp", "localhost:8000")
	if err != nil {
		log.Fatal(err)
	}

	go broadcaster()

	for {
		conn, err := listener.Accept()
		if err != nil {
			log.Print(err)
			continue
		}
		go handleConn(conn)
	}
}

func broadcaster() {
	// Channel is hashable - interesting!
	// This is one of the most important aspects in the program - in each
	// goroutine to handle an incoming connection, it creates a channel and pass it
	// to the broadcaster via =entering=. After using the initial message in the
	// =client= to identify itself, this channel is used to pass the messages to
	// that connection from all other connections
	clients := make(map[client]bool)
	for {
		select {
		case msg := <-messages:
			for cli := range clients {
				cli <- msg
			}
		case cli := <-entering:
			clients[cli] = true
		case cli := <-leaving:
			delete(clients, cli)
			close(cli)
		}
	}
}

func handleConn(conn net.Conn) {
	ch := make(chan string)
	go clientWriter(conn, ch)

	who := conn.RemoteAddr().String()
	ch <- "You are " + who
	messages <- who + " has arrived"
	entering <- ch

	input := bufio.NewScanner(conn)
	// This is a blocking method!!!!??!!!
	for input.Scan() {
		messages <- who + ": " + input.Text()
	}

	leaving <- ch
	messages <- who + " has left"
	conn.Close()
}

func clientWriter(conn net.Conn, ch <-chan string) {
	for msg := range ch {
		// Fuck!
		// Fprintln write message into io.Writer, which is an interface only ask
		// for the method of write, which net.Conn happens to have...
		fmt.Fprintln(conn, msg)
	}
}
