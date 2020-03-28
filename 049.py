# Create a variable called compnum and set the value to 50. Ask the user to enter a number. While their guess
# is not the same as the compnum value, tell them if their guess is too low or toohigh  and ask them to have
# another guess. If they enter the same value as compnum, display the message “Well done, you took [count] attempts”.

i =0
compnum = 50
user_num = int(input("Try to guess a number: "))
while user_num != compnum:
    if user_num > compnum:
        print("Too high")
        user_num = int(input("Try to guess a number: "))
    else:
        print("Too low")
        user_num = int(input("Try to guess a number: "))
    i += 1
i += 1
print(f"Well done, you took {i} attempts")