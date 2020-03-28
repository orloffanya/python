# Set a variable called total to 0. Ask the user to enter five numbers and after each input ask them if they
# want that number included. If they do, then add the number to the total. If they do not want it included,
# don’t add it to the total. After they have entered all five numbers, display the total.

total = 0
print("Please enter 5 numbers")

num1 = int(input("The first number: "))
include = input("Do you want to include this number?").lower()
while include[0] != "y" and include[0] != "n":
    print('You should answer "yes" or "no" to the question')
    include = input("Do you want to include this number?").lower()
if include == "yes":
    total += num1

num2 = int(input("The second number: "))
include = input("Do you want to include this number?").lower()
while include[0] != "y" and include[0] != "n":
    print('You should answer "yes" or "no" to the question')
    include = input("Do you want to include this number?").lower()
if include == "yes":
    total += num2


num3 = int(input("The third number: "))
include = input("Do you want to include this number?").lower()
while include[0] != "y" and include[0] != "n":
    print('You should answer "yes" or "no" to the question')
    include = input("Do you want to include this number?").lower()
if include == "yes":
    total += num3


num4 = int(input("The forth number: "))
include = input("Do you want to include this number?").lower()
while include[0] != "y" and include[0] != "n":
    print('You should answer "yes" or "no" to the question')
    include = input("Do you want to include this number?").lower()
if include == "yes":
    total += num4



num5 = int(input("The fifth number: "))
include = input("Do you want to include this number?").lower()
while include[0] != "y" and include[0] != "n":
    print('You should answer "yes" or "no" to the question')
    include = input("Do you want to include this number?").lower()
if include == "yes":
    total += num5

print(f"your total is {total}")