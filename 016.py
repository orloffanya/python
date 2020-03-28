# Ask the user if it is raining and convert their answer to lower case so it doesn’t matter what case they type it in.
# If they answer “yes”, ask if it is windy. If they answer “yes” to this second question, display the answer
# “It is too windy for an umbrella”, otherwise display the message “Take an umbrella”. If they did not answer yes
# to the first question, display the answer “Enjoy your day”.

rainy = input("Is it raining? ")
windy = input("Is it windy? ")
rainy = rainy.lower()
windy = windy.lower()
if rainy != "yes" and rainy != "no":
    print('Please answer "yes" or "no" to the question')
elif  windy != "yes" and windy != "no":
    print('Please answer "yes" or "no" to the question')
else:
    if rainy == "yes" and windy == "yes":
        print("It is too windy for an umbrella")
    elif rainy == "yes":
        print("take an umbrella")
    else:
        print("Enjoy your day!")