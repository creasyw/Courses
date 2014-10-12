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


;; Questiuon:
;; Write a function that takes in an arbitrary length singly-linked list and
;; returns the pairwise reverse of that list. In other words, if I pass in the
;; list A->B->C->D->E->F the function should return the list B->A->D->C->F->E
;; 
;; This is relatively easy. The most straightforward way is to use Lisp/Scheme/Racket,
;; because the operations of "car" and "cdr" are conceptually alike the structure of 
;; linkedlist. Besides, to make it more similiar to liinkedlist, I just need to
;; implement several minor functions.

(define (pair-reverse lst)
  (define (helper first rest)
    (cond [(null? rest) (cons first '())]
          [(null? (cdr rest)) (list (car rest) first)]
          [#t (cons (car rest) (cons first (helper (cadr rest) (cddr rest))))]))
  (helper (car lst) (cdr lst)))
      
