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

(define (sum3 xs)
  (cond [(null? xs) 0]
        [(number? (car xs)) (+ (car xs) (sum3 (cdr xs)))]
        [#t (+ (sum3 (car xs)) (sum3 (cdr xs)))]))

(define (sum4 xs)
  (cond [(null? xs) 0]
        [(number? (car xs)) (+ (car xs) (sum4 (cdr xs)))]
        [(list? (car xs)) (+ (sum4 (car xs)) (sum4 (cdr xs)))]
        [#t (sum4 (cdr xs))]))

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

#! Delay evaluation
(define (my-if x y z)
  (if x (y) (z)))
(define (fact1 n)
  (my-if (= n 1)
      (lambda () 1)
      (lambda () (* n (fact1 (- n 1))))))
  
(define (max-of-list xs)
  (cond [(null? xs) (error "max-of-list given empty list")]
        [(null? (cdr xs)) (car xs)]
        [#t (let ([tlans (max-of-list (cdr xs))])
              (if (> tlans (car xs))
                  tlans
                  (car xs)))]))
