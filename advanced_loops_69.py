# A particular zoo determines the price of admission based on the age of the guest.
# Guests 2 years of age and less are admitted without charge. Children between 3 and
# 12 years of age cost $14.00. Seniors aged 65 years and over cost $18.00. Admission
# for all other guests is $23.00.
# Create a program that begins by reading the ages of all of the guests in a group
# from the user, with one age entered on each line. The user will enter a blank line to
# indicate that there are no more guests in the group. Then your program should display
# the admission cost for the group with an appropriate message. The cost should be
# displayed using two decimal places.

i = 0
price = 0
flag = False
age = input("Please enter the age of a visitor to calculate ticket price (blank to quit): ")
while age != "":
    age = int(age)
    if age <= 2:
        flag = True
        i -= 1
    elif 3 <= age <= 12:
        price += 14.00
    elif age >= 65:
        price += 18.00
    else:
        price += 23.00
    i += 1
    age = input("Please enter the age of a visitor to calculate ticket price (blank to quit): ")
if flag:
    print(f"Children 2 years and under in your group are submitted free of charge.\n Total price for {i} tickets is {price}")
else:
    print(f"Total price for {i} tickets is {price}")
