#lang racket
(provide (all-defined-out))

; intro
(define (funny-sum xs)
(cond [(null? xs) 0]
      [(number? (car xs)) (+ (car xs) (funny-sum (cdr xs)))]
      [(string? (car xs)) (+ (string-length (car xs) (funny-sum (cdr xs))))]))

; struct
; build a language
(struct bool (b) #:transparent)
(struct eq-num (e1 e2) #:transparent)
(struct if-then-else (e1 e2 e3) #:transparent)
(struct const (int) #:transparent)
(struct negate (e1) #:transparent)
(struct add (e1 e2) #:transparent)
(struct multiply (e1 e2) #:transparent)

(define test1 (multiply (negate (add (const 2)
                                     (const 2)))
                        (const 7)))
(define test2 (multiply (negate (add (const 2)
                                     (const 2)))
                        (if-then-else (bool #f)
                                      (const 7)
                                      (bool #t))))
(define non-test (multiply (negate (add (const #t)
                                        (const 2)))
                           (const 7)))

(define (eval-exp e)
  (cond [(const? e) e]
        [(negate? e) (let ([v (eval-exp (negate-e1 e))])
                       (if (const? v)
                           (const (- (const-int v)))
                           (error "negate applied to non-number")))]
        [(add? e) (let ([v1 (eval-exp (add-e1 e))]
                        [v2 (eval-exp (add-e2 e))])
                    (if (and (const? v1) (const? v2))
                        (const (+ (const-int v1) (const-int v2)))
                        (error "add applied to non-number(s)")))]
        [(multiply? e) (let ([v1 (eval-exp (multiply-e1 e))]
                        [v2 (eval-exp (multiply-e2 e))])
                    (if (and (const? v1) (const? v2))
                        (const (* (const-int v1) (const-int v2)))
                        (error "multiply applied to non-number(s)")))]
        [(bool? e) e]
        [(eq-num? e) (let ([v1 (eval-exp (eq-num-e1 e))]
                          [v2 (eval-exp (eq-num-e2 e))])
                       (if (and (const? v1) (const? v2))
                           (bool (= (const-int v1) (const-int v2)))
                           (error "eq-num applied to non-number(s)")))]
        [(if-then-else? e) (let ([v-test (eval-exp (if-then-else-e1 e))])
                             (if (bool? v-test)
                                 (if (bool-b v-test)
                                     (eval-exp (if-then-else-e2 e))
                                     (eval-exp (if-then-else-e3 e)))
                                 (error "if-then-else applied to non-boolean")))]
        [#t (error "eval-exp expected an exp")]))

; macro
(define (andalso e1 e2)
  (if-then-else e1 e2 (bool #f)))
(define (double e)
  (multiply e (const 2)))
(define (list-product es)
  (if (null? es)
      (const 1)
      (multiply (car es) (list-product (cdr es)))))
(define test3 (andalso (eq-num (double (const 4))
                              (list-product (list (const 2)
                                                  (const 2)
                                                  (const 1)
                                                  (const 2))))
                      (bool #t)))

; eval
(define (make-some-code1 y)
  (if y
      (list 'begin (list 'print "hi") (list '+ 4 2))
      (list '+ 5 3)))
(define (test11) (eval (make-some-code1 #t)))
(define (make-some-code2 y)
  (if y
      (quote (begin (print "Hi") (+ 4 2)))
      (quote (+ 5 3))))
(define (test12) (eval (make-some-code2 #t)))