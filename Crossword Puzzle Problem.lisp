(defparameter *crossword-grid* 
  '((#\- #\G #\- #\H #\T #\M #\L)
    (#\- #\I #\- #\A #\- #\- #\I)
    (#\S #\T #\A #\C #\K #\- #\S)
    (#\M #\- #\- #\K #\- #\- #\P)
    (#\T #\- #\A #\- #\- #\- #\-)
    (#\P #\O #\P #\- #\- #\- #\-)
    (#\- #\- #\I #\D #\E #\- #\-)))

(defparameter *clues*
  '((:across 1 "A data structure with LIFO behavior(5)" STACK)
    (:across 2 "A protocol for sending electronic mail(3)" POP)
    (:across 3 "A fundamental language for web development(4)" HTML)
    (:across 4 "A tool for software development(3)" IDE)
    (:down 5 "A common version control system(3)" GIT)
    (:down 6 "To gain unauthorized access to a computer system(4)" HACK)
    (:down 7 "A set of rules and protocols that allows softwares to communicate with each other(3)" API)
    (:down 8 "A Symbolic language with list processing(4)" LISP)))


(defun print-crossword-grid (grid)
  (format t "~%CROSSWORD PUZZLE: ~%" )
  (format t "(* indicate the cells where the words occur) ~%~%" )
  (loop for row in grid
    do (loop for cell in row
      do (if (char= cell #\-)
             (format t "~a " cell)
             (format t "* ")))
    do (format t "~%")))

(defun print-answer (grid)
    (loop for row in grid
    do (loop for cell in row
             do (format t "~a " cell))
    do (format t "~%")))

(defun check-answer (user-input answer)
      (if (string= user-input answer)
      (format t "RIGHT!~%")
      (progn
        (format t "WRONG. Try again.~%")
        (loop
          (format t "Enter your answer again: ")
          (finish-output)
          (let ((user-input (read-line *query-io*)))
            (if (string= user-input answer)
                (progn
                  (format t "RIGHT!~%")
                  (return)) ; Exit the loop if the answer is correct
                (format t "WRONG. Try again.~%")))))))


(defun play-crossword (clues)
  (format t "Welcome to the crossword puzzle!~%")
  (format t "Let's get started.~%")
  (print-crossword-grid *crossword-grid*)
  (format t "~%CLUES:~%~%")
  (loop for clue in clues
    do (format t "Direction: [~a] ~a~%" (car clue) (caddr clue))
    do (format t "Enter your answer: ")
    do (finish-output)
    do (let ((user-input (read-line *query-io*)))
          (check-answer user-input (cadddr clue))))
  (format t "Congratulations, you've completed the puzzle!~%")
  (print-answer *crossword-grid*)
)

(play-crossword *clues*)


