#lang racket
(require "hw4.rkt") 

(begin (print "Q0101") (ormap eq? (sequence 3 11 2) (list 3 5 7 9 11)))
(begin (print "Q0102") (ormap eq? (sequence 3 8 3) (list 3 6)))
(begin (print "Q0201") (ormap equal? (string-append-map (list "a" "b" "c") "kaka")
			      '("akaka" "bkaka" "ckaka")))
(begin (print "Q0301") (= (list-nth-mod (list 1 2 3 4 5 6) 10) 5))






