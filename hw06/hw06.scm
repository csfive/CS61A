(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cddr s)))

(define (ascending? lst)
  (if (or (null? lst) (null? (cdr lst)))
      #t
      (and (<= (car lst) (cadr lst))
           (ascending? (cdr lst)))))

(define (interleave lst1 lst2)
  (if (null? lst1)
      lst2
      (if (null? lst2)
          lst1
          (cons (car lst1)
                (cons (car lst2)
                      (interleave (cdr lst1) (cdr lst2)))))))

(define (my-filter func lst)
  (if (null? lst)
      '()
      (if (func (car lst))
          (cons (car lst) (my-filter func (cdr lst)))
          (my-filter func (cdr lst)))))

(define (no-repeats lst)
  (if (null? lst)
      lst
      (cons (car lst)
            (my-filter (lambda (x) (not (= x (car lst))))
                       (no-repeats (cdr lst))))))
