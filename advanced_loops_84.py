# What’s the minimum number of times you have to flip a coin before you can have
# three consecutive flips that result in the same outcome (either all three are heads or
# all three are tails)? What’s the maximum number of flips that might be needed? How
# many flips are needed on average? In this exercise we will explore these questions
# by creating a program that simulates several series of coin flips.
# Create a program that uses Python’s random number generator to simulate flipping
# a coin several times. The simulated coin should be fair, meaning that the probability
# of heads is equal to the probability of tails. Your program should flip simulated
# coins until either 3 consecutive heads of 3 consecutive tails occur. Display an H each
# time the outcome is heads, and a T each time the outcome is tails, with all of the
# outcomes for one simulation on the same line. Then display the number of flips that
# were needed to reach 3 consecutive occurrences of the same outcome. When your
# program is run it should perform the simulation 10 times and report the average
# number of flips needed. Sample output is shown below:
# H T T T (4 flips)
# H H T T H T H T T H H T H T T H T T T (19 flips)
# T T T (3 flips)
# T H H H (4 flips)
# H H H (3 flips)
# T H T T H T H H T T H H T H T H H H (18 flips)
# H T T H H H (6 flips)
# T H T T T (5 flips)
# T T H T T H T H T H H H (12 flips)
# T H T T T (5 flips)
# On average, 7.9 flips were needed.


# import random
# i = 0
# g = 0
# result = ""
# for flip_set in range(10):
#     flag = True
#     while flag:
#         flip = random.randint(1, 100)
#         if flip % 2 == 0:
#             outcome = "H"
#         else:
#             outcome = "T"
#         result = result + outcome + " "
#         i += 1
#         if len(result) > 4:
#             for item in range(len(result)-4):
#                 if result[item] != " ":
#                     if result[item] == result[item + 2]:
#                         if result[item] == result[item + 4]:
#                             flag = False
#                             print(f"{result} ({i} flips)")
#                             result = ""
#                             g += i
#                             i = 0
#                             break
# print(f"On average, {g / 10} flips were needed.")


import random


def flip_coin():
    if random.randint(1, 100) % 2 == 0:
        return "H"
    else:
        return "T"


i = 0
g = 0
result = ""
for flip_set in range(10):
    flag = True
    while flag:
        result = result + flip_coin() + " "
        i += 1
        if len(result) > 4:
            for item in range(len(result) - 4):
                if result[item] != " ":
                    if result[item] == result[item + 2]:
                        if result[item] == result[item + 4]:
                            flag = False
                            print(f"{result} ({i} flips)")
                            result = ""
                            g += i
                            i = 0
                            break
print(f"On average, {g / 10} flips were needed.")
