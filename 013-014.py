# Ask the user to enter a number that is under 20. If they enter a number that is 20 or
# more, display the message “Too high”, otherwise display “Thank you”.

number = int(input("Please enter a number that is under 20 "))
if number >= 20:
    print("Too high!")
else:
    print("Thank you!")

# Ask the user to enter a number between 10 and 20 (inclusive). If they enter a number within this range,
# display the message “Thank you”, otherwise display the message “Incorrect answer”.

number = int(input("Please enter a number that is under 20 "))
if number > 20:
    print("Incorrect answer!")
elif number < 10:
    print("Incorrect answer!")
else:
    print("Thank you!")