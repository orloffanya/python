# In this exercise you will create a program that computes the average of a collection
# of values entered by the user. The user will enter 0 as a sentinel value to indicate
# that no further values will be provided. Your program should display an appropriate
# error message if the first value entered by the user is 0.

i = 0
total = 0
print("I will count an average of numbers you enter.\n Just enter 0 when you want me to stop")
number = int(input("Please enter a number: "))
i += 1
while number == 0 and i == 1:
    print("It's too early to quit, we haven't even started")
    number = int(input("Please enter a number: "))
while number != 0:
    total += number
    average = total / i
    print(f"{total} / {i} = {average}")
    number = int(input("Please enter a number: "))
    i += 1
print("Thank you")