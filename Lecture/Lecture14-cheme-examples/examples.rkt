;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-reader.ss" "lang")((modname examples) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(define pi1 3.14)
(define two_pi (* 2 pi1))
(define (square x) (* x x))
(define (sumv x y z) (+ x y z))
(square 5)
(sumv 2 3 4)
(if (> 3 1) (* 8 8) (* 5 5))

(define (leap? year)
   (cond
     ((zero? (modulo year 400)) #t)
     ((zero? (modulo year 100)) #f)
     (else (zero? (modulo year 4)))
))


(define (memberl atm a_list)
	(cond
		((null? a_list) #f)
		((eq? atm (car a_list)) #t)
		(else (memberl atm (cdr a_list)))
	) )   



(define (equalsimp list1 list2)
	(cond
		((null? list1) (null? list2))
		((null? list2) #f)
		((eq? (car list1) (car list2))
			(equalsimp(cdr list1)(cdr list2)))
		(else #f)
	))



(define (equal list1 list2)
	  (cond
		((not (list? list1))(eq? list1 list2))
		((not (list? list2)) #f)
		((null? list1) (null? list2))
		((null? list2) #f)
		((equal (car list1) (car list2))
			(equal (cdr list1) (cdr list2)))
		(else #f)
	))



(define (appendlist list1 list2)
	  (cond
		((null? list1) list2)
		(else (cons (car list1)
			  (append (cdr list1) list2)))
	))

