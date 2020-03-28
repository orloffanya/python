# 29 Ask the user to enter an integer that is over 500. Work
# out the square root of that number and display it to two decimal places.
import math
integer = input("please choose a number whole number over 500 ")
integer = int(integer)
print(f"here is it's square root {round(math.sqrt(integer), 2)}")
