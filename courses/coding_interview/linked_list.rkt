#lang racket

(define (make-linkedlist lst)
  (if (null? lst) '()
      (cons (list-ref lst 0) (make-linkedlist (list-tail lst 1)))))

(define (push x lst) (cons x lst))
(define (look-up x lst)
  (cond [(null? lst) #f]
        [(eq? x (car lst)) #t]
        [#t (look-up x (cdr lst))]))
(define (delete x lst)
  (remove x lst))

(define (pair-reverse lst)
  (define (helper first rest)
    (cond [(null? rest) (cons first '())]
          [(null? (cdr rest)) (list (car rest) first)]
          [#t (cons (car rest) (cons first (helper (cadr rest) (cddr rest))))]))
  (helper (car lst) (cdr lst)))
      