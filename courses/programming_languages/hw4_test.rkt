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



