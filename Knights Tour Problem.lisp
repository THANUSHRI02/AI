(defvar N 8)
(defvar sol nil)
(defvar x-move (vector 2 1 -1 -2 -2 -1  1  2))
(defvar y-move (vector 1 2  2  1 -1 -2 -2 -1))
(defun is-safe? (x y)
  (and (>= x 0) (< x N) (>= y 0) (< y N) (= -1 (aref sol x y))))
(defun print-solution ()
  (format t "Welcome to the Knights problem!~%")
  (format t "Let's display a possible solution.~%")
  (dotimes (x N)
    (dotimes (y N)
      (format t " ~2d " (aref sol x y)))
    (format t "~%")))
(defun solveKnightTour (x y move-i)
  (or (= move-i (* N N))
      (loop for k below N
         :for next-x := (+ x (aref x-move k)) :and
              next-y := (+ y (aref y-move k))
           :if (is-safe? next-x next-y) :do
                 (setf (aref sol next-x next-y) move-i)
                 (if (solveKnightTour next-x next-y (1+ move-i)) (return t)
                     (setf (aref sol next-x next-y) -1)))))
(defun knightTour ()
  (setq sol (make-array (list N N) :initial-element -1))
  (setf (aref sol 0 0) 0)
  (if (solveKnightTour 0 0 1) (print-solution)
      (write "Solution does not exist")))
(knightTour)

