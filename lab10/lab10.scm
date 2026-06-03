(define (over-or-under num1 num2)
  (cond 
    ((> num1 num2) 1)
    ((< num1 num2) -1)
    (else          0)))

(define (make-adder num)
  (lambda (inc) (+ num inc)))

(define (composed f g) (lambda (x) (f (g x))))

(define (square n) (* n n))

(define (pow base exp)
  (cond 
    ((= exp 0)   1)
    ((even? exp) (square (pow base (/ exp 2))))
    (else        (* base (pow base (- exp 1))))))
