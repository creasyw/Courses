;;; Given a positive integer n, find all ordered pairs of distinct
;;; positive integers i and j, where 1<=j<i<=n, s.t. i+j is prime

;;; Find out if a number is prime
(define (smallest-divisor n)
  (find-divisor n 2))
(define (find-divisor n test-divisor)
  (cond ((> (square test-divisor) n) n)
	((divides? test-divisor n) test-divisor)
	(else (find-divisor n (+ test-divisor 1)))))
(define (divides? a b)
  (= (remainder b a) 0))
(define (prime? n)
  (= n (smallest-divisor n)))

;;; basic operation blocks
(define (accumulate op initial sequence)
  (if (null? sequence)
    initial
    (op (car sequence)
	(accumulate op initial (cdr sequence)))))
(define (enumerate-interval low high)
  (if (> low high) ()
    (cons low (enumerate-interval (+ low 1) high))))

;;; specific operation for this question
(define (flat-map proc seq)
  (accumulate append () (map proc seq)))
(define (prime-sum? pair)
  (prime? (+ (car pair) (cadr pair))))
(define (make-pair-sum pair)
  (list (car pair) (cadr pair) (+ (car pair) (cadr pair))))

;;; Main
(define (prime-sum-pairs n)
  (map make-pair-sum
       (filter prime-sum?
	       (flat-map
		 (lambda (i)
		   (map (lambda (j) (list i j))
			(enumerate-interval 1 (- i 1))))
		 (enumerate-interval 1 n)))))



