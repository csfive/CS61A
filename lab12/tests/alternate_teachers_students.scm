(define (student-create name classes) (cons (list name) (list classes)))
(define (teacher-create name class students) (cons (list name) (cons (list class) (list students))))

(define (student-get-name student) (car (car student)))
(define (student-get-classes student) (car (cdr student)))

(define (teacher-get-name teacher) (car (car teacher)))
(define (teacher-get-class teacher) (car (car (cdr teacher))))
(define (teacher-get-students teacher) (car (cdr (cdr teacher))))