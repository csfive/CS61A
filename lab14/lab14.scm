(define (split-at lst n)
  (cond 
    ((= n 0)
     (cons nil lst))
    ((null? lst)
     (cons lst nil))
    (else
     (let ((rec (split-at (cdr lst) (- n 1))))
       (cons (cons (car lst) (car rec)) (cdr rec))))))

; Tree Abstraction
; Constructs tree given label and list of branches
(define (tree label branches)
  (cons label branches))

; Returns the label of the tree
(define (label t) (car t))

; Returns the list of branches of the given tree
(define (branches t) (cdr t))

; Returns #t if t is a leaf, #f otherwise
(define (is-leaf t) (null? (branches t)))

(define (filter-odd t)
  (cond 
    ((null? t)
     nil)
    ((odd? (label t))
     (tree (label t) (map filter-odd (branches t))))
    (else
     (tree nil (map filter-odd (branches t))))))

(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cddr s)))

(define (swap expr)
  (let ((op (car expr))
        (first (car (cdr expr)))
        (second (caddr expr))
        (rest (cdr (cddr expr))))
    (if (> (eval second) (eval first))
        (cons op (cons second (cons first rest)))
        expr)))
