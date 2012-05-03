(define (factorial base product)
  (if (= base 1) product
    (factorial (- base 1) (* product base))))

(define (sum-digit input)
  (define digit-list (string->list (number->string input)))
  (define (accu-digit result left)
    (if (null? left) result
      (accu-digit (+ result (char->digit (car left))) (cdr left))))
  (accu-digit 0 digit-list))

(define (sum-digit-factorial base)
  (sum-digit (factorial base 1)))

