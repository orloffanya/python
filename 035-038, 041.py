# Ask the user to enter their name and then display their name three times.

name = input("Please enter your name: ")
print(f"{name} " * 3)

# Alter program 035 so that it will ask the user to enter their name and a number and then display their name that
# number of times.

number = int(input("How many time should I display it? "))
print(f"{name} " * number)

# Ask the user to enter their name and display each letter in their name on a separate line.

# length = len(name)
# i = 0
# while length > i:
#     print(f"{name[i]} \n")
#     i = i + 1

for letter in name:
    print(letter)


# Change program 037 to also ask for a number. Display their name (one letter at a time on each line) and
# repeat this for the number of times they entered.

# repeat = int(input("How many time should I repeat this? "))
# x = 0
# while repeat > x:
#     i = 0
#     while length > i:
#         print(f"{name[i]} \n")
#         i = i + 1
#     print(f"------ \n")
#     x = x + 1

repeat = int(input("How many time should I repeat this? "))
x = 0
while repeat > x:
    for letter in name:
        print(letter)
    print(f"------ \n")
    x = x + 1

# Ask the user to enter their name and a number. If the number is less than 10, then display their name that
# number of times; otherwise display the message “Too high” three times.

print(f"Your name is {name.title()}")
print(f"You want me to display it {number} times")
if number < 10:
    print(f"{name} " * number)
else:
    print("That's too many times")