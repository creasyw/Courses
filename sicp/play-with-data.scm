(define (list-ref items n)
  (if (= n 0) (car items)
    (list-ref (cdr items) (- n 1))))

(define (length items)
  (define (length-iter a count)
    (if (null? a) count
      (length-iter (cdr a) (+ count 1))))
  (length-iter items 0))

(define (append list1 list2)
  (if (null? list1) list2
    (cons (car list1) (append (cdr list1) list2))))

(define (map proc items)
  (if (null? items) ()
    (cons (proc (car items)) (map proc (cdr items)))))

(define test (list 2 -5 -3 6 -9))
(map abs test)
