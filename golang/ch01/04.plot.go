package main

import (
	"image"
	"image/color"
	"image/gif"
	"io"
	"math"
	"math/rand"
	"os"
)

var palette = []color.Color{color.White, color.Black}

const (
	whiteIndex = 0
	blackIndex = 1
)

func main() {
	// it is cute to simply dump the output to the Stdout...
	// $ ./ch01.04.plot > out.gif
	lissajous(os.Stdout)
}

func lissajous(out io.Writer) {
	const (
		cycles  = 5
		res     = 0.001
		size    = 100
		nframes = 64
		delay   = 8
	)

	freq := rand.Float64() * 3.0
	// https://golang.org/pkg/image/gif/#GIF
	anim := gif.GIF{LoopCount: nframes}
	phase := 0.0
	for i := 0; i < nframes; i++ {
		// func Rect(x0, y0, x1, y1 int) Rectangle
		rect := image.Rect(0, 0, 2*size+1, 2*size+1)
		// func NewPaletted(r Rectangle, p color.Palette) *Paletted
		img := image.NewPaletted(rect, palette)

		for t := 0.0; t < cycles*2*math.Pi; t += res {
			x := math.Sin(t)
			y := math.Sin(t*freq + phase)
			// This is the place to draw the waves in a white board
			// The offset, both "size+" and "+0.5" corresponding to the original
			// rectangle defined above - it is to draw the line from the center
			// of the entire image.
			// SetColorIndex(x, y int, index uint8)
			img.SetColorIndex(size+int(x*size+0.5), size+int(y*size+0.5), blackIndex)
		}
		phase += 0.1
		// Delay []int - The successive delay times, one per frame, in 100ths of a second.
		anim.Delay = append(anim.Delay, delay)
		// Image []*image.Paletted - The successive images.
		anim.Image = append(anim.Image, img)
	}
	gif.EncodeAll(out, &anim)
}
