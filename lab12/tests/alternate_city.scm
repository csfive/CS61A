(define (make-city name lat lon) (cons (cons name (cons lat (cons lon nil))) nil))
(define (get-name city) (car (car city)))
(define (get-lat city) (car (cdr (car city))))
(define (get-lon city) (car (cdr (cdr (car city)))))