(define (cadr lst) (car (cdr lst)))

(define (make-kwlist1 keys values)
  (list keys values))

(define (get-keys-kwlist1 kwlist) (car kwlist))

(define (get-values-kwlist1 kwlist) (cadr kwlist))

(define (make-kwlist2 keys values)
  (if (null? keys)
      nil
      (cons (list (car keys) (car values))
            (make-kwlist2 (cdr keys) (cdr values)))))

(define (get-keys-kwlist2 kwlist)
  (map (lambda (x) (car x)) kwlist))

(define (get-values-kwlist2 kwlist)
  (map (lambda (x) (cadr x)) kwlist))

(define (add-to-kwlist kwlist key value)
  (make-kwlist
   (append (get-keys-kwlist kwlist) (list key))
   (append (get-values-kwlist kwlist) (list value))))

(define (get-first-from-kwlist kwlist key)
  (if (null? (get-keys-kwlist kwlist))
      nil
      (let ((values (get-values-kwlist kwlist))
            (keys (get-keys-kwlist kwlist)))
        (cond 
          ((equal? (car keys) key)
           (car values))
          (else
           (get-first-from-kwlist
            (make-kwlist (cdr keys) (cdr values))
            key))))))

(define (prune-expr expr)
  (define (prune-helper lst)
    (if (or (null? lst) (null? (cdr lst)))
        lst
        (cons (car lst) (prune-helper (cdr (cdr lst))))))
  (cons (car expr) (prune-helper (cdr expr))))

(define (curry-cook formals body)
  (if (null? formals)
      body
      `(lambda (,(car formals))
         ,(curry-cook (cdr formals) body))))

(define (curry-consume curries args)
  (if (null? args)
      curries
      (curry-consume (curries (car args)) (cdr args))))
