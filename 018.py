# Ask the user to enter a number. If it is under 10, display the message “Too low”, if their number is
# between 10 and 20, display “Correct”, otherwise display “Too high”.

number = int(input("Please enter a number "))
if number < 10:
    print("Too low")
elif 10 <= number <= 20:
    print("Correct")
else:
    print("Too high")