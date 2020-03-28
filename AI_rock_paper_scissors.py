import random
i = 0
g = 0
print("Rock...")
print("Paper...")
print("Scissors...")
while True:
    while i < 3 and g < 3:
        player1 = input('Please enter "rock" "paper" or "scissors" ')
        player1 = player1.lower()
        computer = random.randint(1, 3)
        if player1 != "rock" and player1 != "paper" and player1 != "scissors":
            print("Something went wrong!")
        else:
            if computer == 1:
                computer = "rock"
                print("Computer chooses " + computer)
            elif computer == 2:
                computer = "paper"
                print("Computer chooses " + computer)
            else:
                computer = "scissors"
                print("Computer chooses " + computer)
            if player1.lower() == computer:
                print("it's a tie!")
            elif (player1 == "rock" and computer == "paper") or (player1 == "paper" and computer == "scissors") or (player1 == "scissors" and computer == "rock"):
                print("Computer wins!")
                i += 1
            else:
                print("You win!")
                g += 1
    if g == 3:
        print("You have won this set!")
    else:
        print("Computer wins this set! ")
    play_again = input("Do you want to play again? ").lower()
    if play_again[0] != "y":
        print("Thank you!")
        break