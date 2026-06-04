; City Abstraction
(define (make-city name lat lon)
  (cons name (cons lat (cons lon nil))))

(define (get-name city) (car city))

(define (get-lat city) (car (cdr city)))

(define (get-lon city) (car (cdr (cdr city))))

(define (distance city-a city-b)
  (define lat-a (get-lat city-a))
  (define lon-a (get-lon city-a))
  (define lat-b (get-lat city-b))
  (define lon-b (get-lon city-b))
  (sqrt (+ (expt (- lat-a lat-b) 2)
           (expt (- lon-a lon-b) 2))))

(define (closer-city lat lon city-a city-b)
  (if (< (distance city-a (make-city 'temp lat lon))
         (distance city-b (make-city 'temp lat lon)))
      (get-name city-a)
      (get-name city-b)))

; Teacher and Student Abstractions
(define (student-create name classes)
  (cons name classes))

(define (teacher-create name class students)
  (cons name (cons class students)))

(define (student-get-name student) (car student))

(define (student-get-classes student)
  (cdr student))

(define (teacher-get-name teacher) (car teacher))

(define (teacher-get-class teacher)
  (car (cdr teacher)))

(define (teacher-get-students teacher)
  (cdr (cdr teacher)))

(define (student-attend-class student class)
  (student-create (student-get-name student)
                  (cons class (student-get-classes student))))

(define (teacher-hold-class teacher)
  (define new-students
          (map (lambda (student)
                 (student-attend-class student
                                       (teacher-get-class teacher)))
               (teacher-get-students teacher)))
  (teacher-create (teacher-get-name teacher)
                  (teacher-get-class teacher)
                  new-students))

; Rational Abstraction
; Helpers
(define (cadr lst) (car (cdr lst)))

(define (gcd a b)
  (if (= b 0)
      (abs a)
      (gcd b (modulo a b))))

; Creates an object representing the rational number n/d
; Assume: n, d are integers and d != 0
; Note that this constructor simplifies the numerator and denominator
(define (rational n d)
  (let ((g (if (> d 0)
               (gcd n d)
               (- (gcd n d)))))
    (list (/ n g) (/ d g))))

; Gets the numerator of rational number r
(define (numer r) (car r))

; Gets the denominator of rational number r
(define (denom r) (cadr r))

; Adds two rational numbers x and y
(define (add-rational x y)
  (let ((new-num (+ (* (numer x) (denom y))
                    (* (numer y) (denom x))))
        (new-den (* (denom x) (denom y))))
    (rational new-num new-den)))

; Multiply two rational numbers x and y
(define (mul-rational x y)
  (let ((new-num (* (numer x) (numer y)))
        (new-den (* (denom x) (denom y))))
    (rational new-num new-den)))

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
