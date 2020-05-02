;LISP program to display Factorial of a number using iteration
(defun fact(x)
    (setq res 1)
    (loop for i from 1 to x
        do(
            setq res (* res i) 
        )
    )
    res
)
(princ "Enter a number : ")
(setq x (read))
(princ "Factorial of entered number is : ")
(format t " ~D" (fact x))