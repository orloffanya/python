# Ask for a number below 50 and then count down from 50 to that number, making sure you show the number
# they entered in the output.

number = int(input("Please enter a number for countdown to start: "))
i = 50
while number <= i:
    print(i)
    i -= 1
print("Your wife is a smarty pants :)")