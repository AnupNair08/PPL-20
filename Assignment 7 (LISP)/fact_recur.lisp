;LISP program to find factorial using recursion
(defun fact(x)
    (if ( = 1 x)
    1
    (* x (fact (- x 1))))
)
(princ "Enter a number : ")  
(setq x (read))
(princ "Factorial of entered number is : ")
(format t " ~D" (fact x))  