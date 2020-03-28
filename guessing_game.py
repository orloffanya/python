import random

while True:
    comp_number = random.randint(1, 10)
    user_number = int(input("Take a guess: "))
    while comp_number != user_number:
        if comp_number > user_number:
            print("Too low")
        else:
            print("Too high")
        user_number = int(input("Take another guess: "))
    print(f"You guessed it! The number is {comp_number}")
    play_more = input("Do you want to continue playing? ").lower()
    if play_more != "y":
        print("Thank you for playing!")
        break