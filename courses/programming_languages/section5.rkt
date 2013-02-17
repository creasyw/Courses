#lang racket
(provide (all-defined-out))

(define cube1
  (lambda (x) (* x x x)))
(define (cube2 x) (* x x x))

(define (pow1 x y)
  (if (= y 0) 1 (* x (pow1 x (- y 1)))))

(define (sum1 xs)
  (if (null? xs) 0
      (+ (car xs) (sum1 (cdr xs)))))

(define (sum2 xs)
  (if (null? xs)
      0
      (if (number? (car xs))
          (+ (car xs) (sum2 (cdr xs)))
          (if (list? (car xs))
              (+ (sum2 (car xs)) (sum2 (cdr xs)))
              (sum2 (cdr xs))))))

(define (my-append xs ys)
  (if (null? xs)
      ys
      (cons (car xs) (my-append (cdr xs) ys))))

(define (my-map f xs)
  (if (null? xs)
      null
      (cons (f (car xs)) (my-map f (cdr xs)))))

(define (fact n)
  (define (fact-helper n acc)
    (if (= n 0)
        acc
        (fact-helper (- n 1) (* acc n))))
  (fact-helper n 1))
