# Using the song “10 green bottles”, display the lines “There are [num] green bottles
# hanging on the wall, [num] green bottles hanging on the wall, and if 1 green bottle
# should accidentally fall”. Then ask the question “how many green bottles will be
# hanging on the wall?” If the user answers correctly, display the message “There will be
# [num] green bottles hanging on the wall”. If they answer incorrectly, display the
# message “No, try again” until they get it right. When the number of green bottles gets
# down to 0, display the message “There are no more green bottles hanging on the wall”.

# i = 10
# print("Sing along...")
# while i != 0:
#     print(f"There are {i} green bottles\nHanging on the wall\n{i} green bottles hanging on the wall\nAnd if one green bottle\nShould accidentally fall \n")
#     i -= 1
#     number = int(input("How many green bottles will be hanging on the wall? \n"))
#     while number != i:
#         print("Try again")
#         number = int(input("How many green bottles will be hanging on the wall? \n"))
# if number == 0:
#     print("There are no more green bottles hanging on the wall")


print("Sing along...")
for i in range(10, 0, -1):
    number = i
    if i != 1:
        print(f"There are {i} green bottles\nHanging on the wall\n{i} green bottles hanging on the wall\nAnd if one green bottle\nShould accidentally fall \n")
    else:
        print(f"There are {i} green bottle\nHanging on the wall\n{i} green bottle hanging on the wall\nAnd if one green bottle\nShould accidentally fall \n")
    g = i - 1
    if number - 1 != 0:
        number = int(input("How many green bottles will be hanging on the wall? \n"))
        while number != g:
            print("Try again")
            number = int(input("How many green bottles will be hanging on the wall? \n"))
    else:
        print("There'll be no green bottles\nHanging on the wall")




