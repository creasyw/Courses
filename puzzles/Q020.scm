(define (factorial base product)
  (if (= base 1) product
    (factorial (- base 1) (* product base))))

(define (sum-digit input)
  (define (accu-digit result left)
    (if (null? left) result
      (accu-digit (+ result (char->digit (car left))) (cdr left))))
  (let ((digit-list (string->list (number->string input))))
    (accu-digit 0 digit-list)))

(define (sum-digit-factorial base)
  (sum-digit (factorial base 1)))

