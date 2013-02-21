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

;; Delay and Force
(define (my-delay th)
  (mcons #f  th))
(define (my-force p)
  (if (mcar p)
      (mcdr p)
      (begin (set-mcar! p #t)
             (set-mcdr! p ((mcdr p)))
             (mcdr p))))

;; Stream
(define ones(lambda() (cons 1 ones)))
(define (f x) (cons x (lambda () (f (+ x 1)))))
(define powers-of-two
  (letrec ([f  (lambda (x) (cons x (lambda () (f (* x 2)))))])
    (lambda () (f 2))))

; Another factorial with streaming
(define (g acc x) (cons acc (lambda () (g (* x acc)(+ x 1)))))
(define (fact2 stream n)
  (letrec ([f (lambda (stream ans)
             (let ([pr (stream)])
               (if (>= ans n)
                   (car pr)
                   (f (cdr pr) (+ ans 1)))))])
    (f stream 1)))
; Test
(fact2 (cdr (g 1 1)) 10)

; Memozation
(define fibonacci
  (letrec ([memo null]
           [f (lambda (x)
                (let ([ans (assoc x memo)])
                  (if ans
                      (cdr ans)
                      (let ([new-ans (if (or (= x 1) (= x 2))
                                         1
                                         (+ (f (- x 1))
                                            (f (- x 2))))])
                        (begin
                          (set! memo (cons (cons x new-ans) memo))
                          new-ans)))))])
    f))

; micro
(define-syntax my-ifs
  (syntax-rules (then else)
    [(my-if e1 then e2 else e3)
     (if e1 e2 e3)]))