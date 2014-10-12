
#lang racket

(provide (all-defined-out)) ;; so we can put tests in a second file

;; put your code below

;; prob 1
(define (sequence low high stradle)
  (if (> low high) null
      (cons low (sequence (+ low stradle) high stradle))))

;; prob 2
;; constraints: must use string-append(), map()
(define (string-append-map xs suffix)
  (map (lambda (x) (string-append x suffix)) xs))

;; prob 3
(define (list-nth-mod xs n)
  (cond [(< n 0) (error "list-nth-mod: negative number")]
        [(= 0 (length xs)) (error "list-nth-mod: empty list")]
        [#t (car (list-tail xs (remainder n (length xs))))])) 

;; prob 4
(define (stream-for-n-steps s n)
  (letrec ([pr (s)])
    (if (= n 0) null
        (cons (car pr) (stream-for-n-steps (cdr pr) (- n 1))))))

;; prob 5
(define funny-number-stream 
  (letrec ([-num (lambda (n) (if (= 0 (remainder n 5)) (- n) n))]
           [f (lambda (x) (cons (-num x) (lambda () (f (+ x 1)))))])
    (lambda () (f 1))))


;; prob 6
(define dan-then-dog (letrec ([dan-or-dog (lambda (x) (if (= 0 (remainder x 2)) "dan.jpg" "dog.jpg"))]
                              [f (lambda (x)
                                   (cons (dan-or-dog x) (lambda () (f (+ x 1)))))])
                       (lambda () (f 0))))

;; prob 7
(define (stream-add-zero stream-in)
  (letrec ([f (lambda(s) (cons (cons 0 (car (s))) (lambda () (f (cdr (s))))))])
    (lambda() (f stream-in))))

;; prob 8
(define (cycle-lists xs ys)
  (letrec ([f (lambda (n) (cons (cons (list-nth-mod xs n) (list-nth-mod ys n))
                                (lambda () (f (+ n 1)))))])
    (lambda () (f 0))))

;; prob 9  
(define (vector-assoc v vec)
  (letrec ([h (lambda (i) 
                (let ([curr-elem (vector-ref vec i)])
                  (cond 
                    [(and (pair? curr-elem) (equal? v (car curr-elem))) (cons (car curr-elem) (cdr curr-elem))] ;; check if curr-elem is v
                    [(= (+ i 1) (vector-length vec)) #f] ;; we've exhausted the vector: return false
                    [#t (h (+ i 1))] ;; still looking, call h again with the index of the next elem
                    )))])
    (if (= 0 (vector-length vec)) #f (h 0))))

;; prob 10
(define (cached-assoc xs n)
  (letrec ([cache (make-vector n #f)]
           [cache-slot 0]
           [f (lambda (x) 
                (let ([cached-ans (vector-assoc x cache)])
                  (if cached-ans 
                      cached-ans
                      (let ([ans (assoc x xs)])
                        (when ans                  
                          (vector-set! cache cache-slot ans) ;; update the cache in-place
                          (set! cache-slot (remainder (+ cache-slot 1) n))) ;; update the next cache-slot
                        ans))))])
    f))

;; prob 11 : Challenge
(define-syntax while-less
  (syntax-rules (do)
    [(while-less e1 do e2)
     (letrec ([e1val e1]
              [f (lambda () 
                   (if (<= e1val e2) #t (f)))])
       (f))]))







