;LISP Program to find nth element of a list
(defun getX(n x)
(
    if( = n 1)
    (first x)
    (getX (- n 1) (rest x ))
    
)
)
(princ "Enter the list : ")
(setq x (read-from-string (concatenate 'string "(" (read-line) ")")))
(princ "Enter n : ")
(setq n (read))
(format t "~Dth element is : " n)
(write (getX n x))