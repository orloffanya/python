# for x in range(1, 21):
#     if x == 4 or x == 13:
#         print(f"{x} is UNLUCKY!")
#     elif x % 2 == 0:
#         print(f"{x} is even")
#     else:
#         print(f"{x} is odd")

for number in range(1, 21):
    if number == 4 or number == 13:
        x = "UNLUCKY!"
    elif number % 2 == 0:
        x = "even"
    else:
        x = "odd"
    print(f"{number} is {x}")