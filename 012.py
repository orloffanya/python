# Ask for two numbers. If the first one is larger than the second, display the second number first
# and then the first number, otherwise show the first number first and then the second.
number1 = int(input("Please enter a number "))
number2 = int(input("Please input another number "))
if number1 == number2:
    print("They are equal")
elif number1 > number2:
    print(f"number2 is larger than number1 \n{number2}\n{number1}")
else:
    print(f"number1 is larger than number2 \n{number1}\n{number2}")