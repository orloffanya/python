# Ask the user to enter two numbers. Use whole number division to divide
# the first number by the second and also work out the remainder and
# display the answer in a user-friendly way (e.g. if they enter 7 and 2 display
# “7 divided by 2 is 3 with 1 remaining”).

number1 = int(input("please enter a number "))
number2 = int(input("please enter another number "))
division = number1 / number2
division = int(division)
remainder = number1 % number2
print(f"{number1} divided by {number2} is {division} with {remainder} remaining")
 