# Ask how many people the user wants to invite to a party. If they enter a number below
# 10, ask for the names and after each name display “[name] has been invited”. If they
# enter a number which is 10 or higher, display the message “Too many people”.

i = 0
number = int(input("How many people do you want to invite? "))
if number >= 10:
    print("Too many people")
else:
    i = 0
    total_invited = ""
    while i < number:
        name = input("Please enter the name of a person invited: ")
        print(f"{name.title()} is invited")
        total_invited = total_invited + f"\n{name.title()}"
        i += 1
print("You have invited:")
print(total_invited)


# Ask for the name of somebody the user wants to invite to a party. After this, display the message “[name] has
# now been invited” and add 1 to the count. Then ask if they want to invite somebody else. Keep repeating this
# until they no longer want to invite anyone else to the party and then display how many people they have
# coming to the party.

i = 0
total_invited = ""
name = input("Please enter the name of a person invited: ")
print(f"{name.title()} is invited")
total_invited = total_invited + f"\n{name.title()}"
i += 1
add_question = input("Do you want to invite somebody else? ").lower()
while add_question[0] == "y":
    name = input("Please enter the name of a person invited: ")
    print(f"{name.title()} is invited")
    total_invited = total_invited + f"\n{name.title()}"
    i += 1
    add_question = input("Do you want to invite somebody else? ").lower()
print(f"You have invited {i} people:")
print(total_invited)
