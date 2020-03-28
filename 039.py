# Ask the user to enter a number between 1 and 12 and then display the times table for that number.

# number = int(input("Please enter a number between 1 and 12: "))
# i = 0
# if 1 <= number <= 12:
#     while i < 13:
#         print(f"{i} * {number} = {number * i}")
#         i += 1
# else:
#     print("The times table only works for numbers between 1 and 12")

number = int(input("Please enter a number between 1 and 12: "))
if 1 <= number <= 12:
    for i in range(1, 13):
        print(f"{i} * {number} = {number * i}")
else:
    print("The times table only works for numbers between 1 and 12")