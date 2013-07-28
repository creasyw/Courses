(define (search f neg-point pos-point)
  (let ((midpoint (average neg-point pos-point)))
    (if (close-enough? neg-point pos-point) midpoint
      (let ((test-value (f midpoint)))
	(cond ((positive? test-value)
	       (search f neg-point midpoint))
	      ((negative? test-value)
	       (search f midpoint pos-point))
	      (else midpoint))))))

(define (average x y) (/ (+ x y) 2))

(define (close-enough? x y)
  (< (abs (- x y)) tolerance))

(define (half-interval-method f a b)
  (let ((a-value (f a))
	(b-value (f b)))
    (cond ((and (negative? a-value) (positive? b-value))
	   (search f a b))
	  ((and (negative? b-value) (positive? a-value))
	   (search f b a))
	  (else (error "Value are not of opposite sign" a b)))))

(define tolerance 0.00001)

(define (fixed-point f first-guess)
  (define (try guess)
    (let ((next (f guess)))
      (if (close-enough? guess next) next
	(try next))))
  (try first-guess))

(define (average-damp f)
  (lambda (x) (average x (f x))))

;;; test
(fixed-point (lambda (y) (+ (sin y) (cos y))) 1.0)

(define (sqrt x)
  (fixed-point (average-damp (lambda (y) (/ x y)))
	       1.0))

