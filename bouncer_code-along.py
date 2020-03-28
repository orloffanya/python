#ask for age
age = input("How old are you: ")

if age:
    age = int(age)
    if 18 <= age < 21:
        # 18-21 wristband
        print("You can enter, but need a wristband")
    elif age >= 21:
        # 21+ normal entry
        print("you are good to enter and can drink")
    else:
        # too young
        print("You can't come in, little one! :(")
else:
    print("Please enter your age")

