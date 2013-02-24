#lang racket

(provide (all-defined-out)) ;; so we can put tests in a second file

;; put your code below

; 1
(define (sequence low high stride)
  (if (> low high)
      null
      (cons low (sequence (+ low stride) high stride))))

; 2
(define (string-append-map xs suffix)
  (map (lambda (x) (string-append x suffix)) xs))

; 3
(define (list-nth-mod xs n)
  (cond [(< n 0) (error "list-nth-mod: negative number")]
        [(null? xs) (error "list-nth-mod: empty list")]
        [#t (car (list-tail xs (remainder n (length xs))))]))

; 4
(define (stream-for-n-steps s n)
  (define (g st acc count)
    (let ([pr (st)])
      (if (<= count 0)
          acc
          (g (cdr pr) (cons (car pr) acc) (- count 1)))))
  (reverse (g s '() n)))

; 5
(define funny-number-stream
  (letrec ([f (lambda (x) (cons
                           (if (= (modulo x 5) 0) (- 0 x) x)
                           (lambda () (f (+ x 1)))))])
    (lambda () (f 1))))

; 6
(define dan-then-dog 
  (letrec ([p (list "dan.jpg" "dog.jpg")]
           [f (lambda(x) (cons (car x) (lambda () (f (reverse x)))))])
    (lambda () (f p))))

; 7
(define (stream-add-zero s)
  (letrec ([f (lambda (x) (cons (cons 0 (car (x))) (lambda () (f (cdr (x))))))])
    (lambda () (f s))))

; 8
(define (cycle-lists xs ys)
  (define (streaming-list lst1 n1 lst2 n2)
    (cons (cons (list-ref lst1 (modulo n1 (length lst1))) (list-ref lst2 (modulo n2 (length lst2))))
          (lambda () (streaming-list lst1 (+ n1 1) lst2 (+ n2 1)))))
  (lambda () (streaming-list xs 0 ys 0)))
  
; 9
(define (vector-assoc v vc)
  (define (vector-recursive ind)
    (cond [(<= (vector-length vc) ind) #f]
          [(and (pair? (vector-ref vc ind)) 
                (equal? v (car (vector-ref vc ind)))) 
           (vector-ref vc ind)]
          [#t (vector-recursive (+ ind 1))]))
  (vector-recursive 0))

