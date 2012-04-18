(define (gcd a b)
  (if (= b 0) a
    (gcd b (remainder a b))))

;;; test
(gcd 206 40)
