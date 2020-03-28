# Exercise 52 includes a table that shows the conversion from letter grades to grade
# points at a particular academic institution. In this exercise you will compute the
# grade point average of an arbitrary number of letter grades entered by the user. The
# user will enter a blank line to indicate that all of the grades have been provided. For
# example, if the user enters A, followed by C+, followed by B, followed by a blank
# line then your program should report a grade point average of 3.1.
# You may find your solution to Exercise 52 helpful when completing this exercise.
# Your program does not need to do any error checking. It can assume that each value
# entered by the user will always be a valid letter grade or a blank line.

total = 0
i = 0
average = 0
grade = input("Please enter your grade (Space to quit): ")
while grade != "":
    if grade.upper() == "A":
        total += 4.0
    elif grade.upper() == "A-":
        total += 3.7
    elif grade.upper() == "B+":
        total += 3.3
    elif grade.upper() == "B":
        total += 3.0
    elif grade.upper() == "B-":
        total += 2.7
    elif grade.upper() == "C+":
        total += 2.0
    elif grade.upper() == "C":
        total += 1.7
    elif grade.upper() == "C-":
        total += 1.3
    elif grade.upper() == "D-":
        total += 1.0
    else:
        print("I don't understand")
        i -= 1
    grade = input("Please enter your grade (Space to quit): ")
    i += 1
if i > 0:
    average = total / i
print(f"Your average of {i} grades is {round(average, 1)}")