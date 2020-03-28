print("Rock...")
print("Paper...")
print("Scissors...")
player1 = input('Please enter "rock" "paper" or "scissors" ')
print("********NO CHEATING******\n" * 20)
player2 = input('Please enter "rock" "paper" or "scissors" ')
print("SHOOT!")
if player1 != "rock" and player1 != "paper" and player1 != "scissors":
    print("Something went wrong with player 1!")
elif player2 != "rock" and player2 != "paper" and player2 != "scissors":
    print("Something went wrong with player 2!")
else:
    if player1 == player2:
        print("It's a tie!")
    else:
        if player1 == "rock":
            if player2 == "paper":
                print("Player 2 wins!")
            else:
                print("Player 2 wins!")
        elif player1 == "paper":
            if player2 == "rock":
                print("Player 1 wins!")
            else:
                print("Player 2 wins!")
        elif player1 == "scissors":
            if player2 == "rock":
                print("Player 2 wins!")
            elif player2 == "paper":
                print("Player 1 wins!")

