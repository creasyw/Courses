;;; Adding tags for the selector
(define (attach-tag type-tag contents)
  (cons type-tag contents))

(define (type-tag datum)
  (if (pair? datum) (car datum)
    (error "Bad tagged datum -- TYPE-TAG" datum)))

(define (contents datum)
  (if (pair? datum) (cdr datum)
    (error "Bad tagged datum -- CONTENTS" datum)))

(define (rectangular? z)
  (eq? (type-tag z) 'rectangular))

(define (polar? z)
  (eq? (type-tag z) 'polar))

;;; Customized Constructor
(define (real-part-rectangular z) (car z))
(define (image-part-rectangular z) (cdr z))

(define (magnitude-rectangular z)
  (sqrt (+ (square (real-part-rectangular z))
	   (square (image-part-rectangular z)))))
(define (angle-rectangular z)
  (atan (image-part-rectangular z)
	(real-part-rectangular z)))

;;; Taking care for the other implementation
(define (real-part-polar z)
  (* (magnitude-polar z) (cos (angle-polar z))))

(define (image-part-polar z)
  (* (magnitude-polar z) (sin (angle-polar z))))

(define (angle-polar z) (cdr z))
(define (magnitude-polar z) (car z))

;;; Transformation two implementations into one constructor
(define (make-from-real-image-rectanguar x y)
  (attach-tag 'rectangular (cons x y)))

(define (make-from-mag-ang-rectangular r a)
  (attach-tag 'rectangular (cons (* r (cos a)) (* r (sin a)))))

(define (make-from-real-image-polar x y)
  (attach-tag 'polar (cons (sqrt (+ (square x) (square y))) (atan y x))))

(define (make-from-mag-ang-polar r a)
  (attach-tag 'polar (cons r a)))

;;; Selectors: Generic interface procedure
(define (real-part z)
  (cond ((rectangular? z)
	 (real-part-rectangular (contents z)))
	((polar? z)
	 (real-part-polar (contents z)))
	(else (error "Unknow type -- REAL-PART" z))))

(define (image-part z)
  (cond ((rectangular? z)
	 (image-part-rectangular (contents z)))
	((polar? z)
	 (image-part-polar (contents z)))
	(else (error "Unknow type -- IMAGE-PART" z))))

(define (magnitude z)
  (cond ((rectangular? z)
	 (magnitude-rectangular (contents z)))
	((polar? z)
	 (magnitude-polar (contents z)))
	(else (error "Unknow type -- MAGNITUDE" z))))

(define (angle z)
  (cond ((rectangular? z)
	 (angle-rectangular (contents z)))
	((polar? z)
	 (angle-polar (contents z)))
	(else (error "Unknow type -- IMAGE-PART" z))))

;;; Now the Basic Operations
(define (add-complex z1 z2)
  (make-from-real-image (+ (real-part z1) (real-part z2))
			(+ (image-part z1) (image-part z2))))

(define (sub-complex z1 z2)
  (make-from-real-image (- (real-part z1) (real-part z2))
			(- (image-part z1) (image-part z2))))

(define (mul-complex z1 z2)
  (make-from-mag-ang (* (magnitude z1) (magnitude z2))
		     (+ (angle z1) (angle z2))))

(define (div-complex z1 z2)
  (make-from-mag-ang (/ (magnitude z1) (magnitude z2))
		     (- (angle z1) (angle z2))))

(define (make-from-real-image x y)
  (make-from-real-image-rectangular x y))

(define (make-from-mag-ang r a)
  (make-from-mag-ang-polar r a))

