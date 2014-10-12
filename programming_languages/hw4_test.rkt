#lang racket
(require "hw4.rkt") 

(begin (print "q0101") (ormap eq? (sequence 3 11 2) (list 3 5 7 9 11)))
(begin (print "q0102") (ormap eq? (sequence 3 8 3) (list 3 6)))
(begin (print "q0201") (ormap equal? (string-append-map (list "a" "b" "c") "kaka")
			      '("akaka" "bkaka" "ckaka")))
(begin (print "q0301") (= (list-nth-mod (list 1 2 3 4 5 6) 10) 5))

(define ones(lambda() (cons 1 ones)))
(begin (print "q0401") (ormap eq? (stream-for-n-steps ones 10)
			      '(1 1 1 1 1 1 1 1 1 1)))
(define (accumulator x) (lambda () (cons x (accumulator (+ x 1)))))
(begin (print "q0402") (ormap eq? (stream-for-n-steps (accumulator 1) 10)
			      '(1 2 3 4 5 6 7 8 9 10)))
(begin (print "q0501") (ormap eq? (stream-for-n-steps funny-number-stream 10)
			      '(1 2 3 4 -5 6 7 8 9 -10)))

(define vc1 (vector '(1 2) 10 '(3 4) '(5 6)))
(begin (print "q0901") (ormap eq? (vector-assoc 3 vc1) '(3 4)))
(define vc2 (vector '("a" 2) 10 '(3 4) '("b" 6)))
(begin (print "q0902") (ormap eq? (vector-assoc "b" vc2) '("b" 6)))


;; A simple library for displaying a 2x3 grid of pictures: used
;; for fun in the tests below (look for "Tests Start Here").

(require (lib "graphics.rkt" "graphics"))

(open-graphics)

(define window-name "Programming Languages, Homework 4")
(define window-width 700)
(define window-height 500)
(define border-size 100)

(define approx-pic-width 200)
(define approx-pic-height 200)
(define pic-grid-width 3)
(define pic-grid-height 2)

(define (open-window)
  (open-viewport window-name window-width window-height))

(define (grid-posn-to-posn grid-posn)
  (when (>= grid-posn (* pic-grid-height pic-grid-width))
    (error "picture grid does not have that many positions"))
  (let ([row (quotient grid-posn pic-grid-width)]
        [col (remainder grid-posn pic-grid-width)])
    (make-posn (+ border-size (* approx-pic-width col))
               (+ border-size (* approx-pic-height row)))))

(define (place-picture window filename grid-posn)
  (let ([posn (grid-posn-to-posn grid-posn)])
    ((clear-solid-rectangle window) posn approx-pic-width approx-pic-height)
    ((draw-pixmap window) filename posn)))

(define (place-repeatedly window pause stream n)
  (when (> n 0)
    (let* ([next (stream)]
           [filename (cdar next)]
           [grid-posn (caar next)]
           [stream (cdr next)])
      (place-picture window filename grid-posn)
      (sleep pause)
      (place-repeatedly window pause stream (- n 1)))))

;; Tests Start Here

; These definitions will work only after you do some of the problems
; so you need to comment them out until you are ready.
; Add more tests as appropriate, of course.

(define nums (sequence 0 5 1))

(define files (string-append-map 
               (list "dan" "dog" "curry" "dog2") 
               ".jpg"))

(define funny-test (stream-for-n-steps funny-number-stream 16))

; a zero-argument function: call (one-visual-test) to open the graphics window, etc.
(define (one-visual-test)
  (place-repeatedly (open-window) 0.5 (cycle-lists nums files) 27))

; similar to previous but uses only two files and one position on the grid
(define (visual-zero-only)
  (place-repeatedly (open-window) 0.5 (stream-add-zero dan-then-dog) 27))


(define a 2)
(while-less 7 do (begin (set! a (+ a 1)) (print "x") a))
(while-less 7 do (begin (set! a (+ a 1)) (print "x") a))


