(load "data-directed-programming.scm")

(define (install-rectangular-package)
  ;;; internal procedure
  (define (real-part z) (car z))
  (define (image-part z) (cdr z))
  (define (make-from-real-image x y) (cons x y))
  (define (magnitude z)
    (sqrt (+ (square (real-part z))
	     (square (image-part z)))))
  (define (angle z)
    (atan (image-part z) (real-part z)))
  (define (make-from-mag-ang r a)
    (cons (* r (cos a)) (* r (sin a))))

  (define (tag x) (attach-tag 'rectangular x))
  (put 'real-part '(rectangular) real-part)
  (put 'image-part '(rectangular) image-part)
  (put 'magnitude '(rectangular) magnitude)
  (put 'angle '(rectangular) angle)
  (put 'make-from-real-image 'rectangular
       (lambda (x y) (tag (make-from-real-image x y))))
  (put 'make-from-mag-ang 'rectangular
       (lambda (r a) (tag (make-from-mag-ang r a))))
  'dane)

(define (apply-generic op . args)
  (let ((type-tags (map type-tag args)))
    (let ((proc (get op type-tags)))
      (if proc
	(apply proc (map contents args))
	(error
	  "No method for these types -- APPLY-GENERIC"
	  (list op type-tags))))))

(define (real-part z) (apply-generic 'real-part z))
(define (image-part z) (apply-generic 'image-part z))
(define (magnitude z) (apply-generic 'magnitude z))
(define (angle z) (apply-generic 'angle z))

(define (make-from-real-image x y)
  ((get 'make-from-real-image 'rectangular) x y))

(define (make-from-mag-ang r a)
  ((get 'make-from-mag-ang 'polar) r a))
