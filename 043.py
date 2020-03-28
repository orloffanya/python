# Ask which direction the user wants to count (up or down). If they select up, then ask
# them for the top number and then count from 1 to that number. If they select down, ask
# them to enter a number below 20 and then count down from 20 to that number. If they
# entered something other than up or down, display the message “I don’t understand”.
#
# direction = input("Do you want to count up or down? ").lower()
# if direction == "up":
#     number = int(input("Give me the top number: "))
#     i = 0
#     while i <= number:
#         print(i)
#         i += 1
# elif direction == "down":
#     number = int(input("Select a number below 20: "))
#     if number > 20:
#         print("Too high")
#     else:
#         i = 20
#         while i >= number:
#             print(i)
#             i -= 1
# else:
#     while direction != "up" and direction != "down":
#         print("I don't understand")
#         direction = input("Do you want to count up or down? ").lower()


direction = input("Do you want to count up or down? ").lower()
if direction == "up":
    number = int(input("Give me the top number: "))
    for count in range(1, number + 1):
        print(count)
elif direction == "down":
    number = int(input("Select a number below 20: "))
    if number > 20:
        print("Too high")
    else:
        for count in range(20, number - 1, -1):
            print(count)
else:
    while direction != "up" and direction != "down":
        print("I don't understand")
        direction = input("Do you want to count up or down? ").lower()
