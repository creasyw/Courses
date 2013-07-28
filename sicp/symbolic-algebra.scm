;; Load the put and get
(load "data-directed-programming.scm")

(define (install-polynomial-package)
  ;; internal procedure
  ;; representation of poly
  (define (make-poly variable term-list)
    (cons variable term-list))
  (define (variable p) (car p))
  (define (term-list p) (cdr p))
  (define (variable? x) (symbol? x))
  (define (same-variable v1 v2)
    (and (variable? v1) (variable? v2) (eq? v1 v2)))

  (define (add-ploy p1 p2)
    (if (same-variable? (variable p1) (variable p2))
      (make-poly (variable p1)
		 (add-terms (term-list p1) (term-list p2)))
      (error "Ploys not in same var -- ADD-PLOY" (list p1 p2))))

  (define (mul-poly p1 p2)
    (if (same-variable? (variable p1) (variable p2))
      (make-poly (variable p1)
		 (mul-terms (term-list p1) (term-list p2)))
      (error "Ploys not in same var -- MUL-PLOY" (list p1 p2))))

  (define (adjoin-term term term-list)
    (if (= 0 (coeff term)) term-list
      (cons term term-list)))
  
  (define (the-empty-termlist) '())
  (define (first-term term-list) (car term-list))
  (define (rest-terms term-list) (cdr term-list))
  (define (empty-termlist? term-list) (null? term-list))

  (define (make-term order coeff) (list order coeff))
  (define (order term) (car term))
  (define (coeff term) (cadr term))

  (define (tag p) (attach-tag 'polynomial p))
  (put 'add '(polynomial polynomial)
       (lambda (p1 p2) (tag (add-poly p1 p2))))
  (put 'mul '(polynomial polynomial)
       (lambda (p1 p2) (tag (mul-poly p1 p2))))
  (put 'make 'polynomial
       (lambda (var terms) (tag (make-poly var terms))))
  'done)

(define (add-terms l1 l2)
  (cond ((empty-termlist? l1) l2)
	((empty-termlist? l2) l1)
	(else
	  (let ((t1 (first-term l1)) (t2 (first-term l2)))
	    (cond ((> (order t1) (order t2))
		   (adjoin-term t1 (add-terms (rest-terms l1) l2)))
		  ((< (order t1) (order t2))
		   (adjoin-term t2 (add-terms (rest-terms l2) l1)))
		  (else
		    (adjoin-term
		      (make-term (order t1) (add (coeff t1) (coeff t2)))
		      (make-term (rest-terms l1) (rest-terms l2)))))))))

(define (mul-terms l1 l2)
  (if (empty-termlist? l1) (the-empty-termlist)
    (add-terms (mul-term-by-all-terms (first-term l1) l2)
	       (mul-terms (rest-terms l1) l2))))

(define (mul-term-by-all-terms t1 l)
  (if (empty-termlist? l) (the-empty-termlist)
    (let ((t2 (first-term l)))
      (adjoin-term (make-term (+ (order t1) (order t2)) (mul (coeff t1) (coeff t2)))
		   (mul-term-by-all-terms t1 (rest-terms l))))))

(define (make-polynomial var terms)
  ((get 'make 'polynomial) var terms))

