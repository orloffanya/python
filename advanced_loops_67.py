# Write a program that computes the perimeter of a polygon. Begin by reading the
# x and y coordinates for the first point on the perimeter of the polygon from the
# user. Then continue reading pairs of values until the user enters a blank line for the
# x-coordinate. Each time you read an additional coordinate you should compute the
# distance to the previous point and add it to the perimeter. When a blank line is entered
# for the x-coordinate your program should add the distance from the last point back
# to the first point to the perimeter. Then the perimeter should be displayed. Sample
# input and output values are shown below. The input values entered by the user are
# shown in bold.
# Enter the first x-coordinate: 0
# Enter the first y-coordinate: 0
# Enter the next x-coordinate (blank to quit): 1
# Enter the next y-coordinate: 0
# Enter the next x-coordinate (blank to quit): 0
# Enter the next y-coordinate: 1
# Enter the next x-coordinate (blank to quit):
# The perimeter of that polygon is 3.414213562373095

import math
x = ""
perimeter = 0
print("Let's compute the perimeter of a polygon...")
x = input("Please enter x-coordinate: ")
while x == "":
    print("It's too early to quit, we haven't even started yet")
    x = input("Please enter the first x-coordinate: ")
y = float(input("Please enter the first y-coordinate: "))
y_first = y
x_first = float(x)
x_previous = x_first
y_previous = y_first
while x != "":
    x_previous = float(x)
    y_previous = float(y)
    x = input("Please enter the next x-coordinate: ")
    if x == "":
        if x_previous != x_first and y != y_first:  # count hypotenuse
            cathetus1 = abs(y - y_first)
            cathetus2 = abs(x_previous - x_first)
            hypotenuse = math.sqrt((cathetus1 ** 2) + (cathetus2 ** 2))
            # print(f"x is empty: {hypotenuse} = sqr ({cathetus1} + {cathetus2})")
            perimeter += hypotenuse
        elif x_previous != x_first and y == y_first:
            length = abs(x_previous - x_first)
            perimeter += length
        elif x_previous == x_first and y != y_first:
            length = abs(y - y_first)
            perimeter += length
        print(f"The perimeter of that polygon is {perimeter}")
        break
    else:
        x = float(x)
    y = float(input("Please enter the next y-coordinate: "))
    if x != x_previous and y != y_previous: #count hypotenuse
        cathetus1 = abs(y - y_previous)
        cathetus2 = abs(x - x_previous)
        hypotenuse = math.sqrt((cathetus1 ** 2) + (cathetus2 ** 2))
        # print(f"x is  not empty: {hypotenuse} = sqr ({cathetus1} + {cathetus2})")
        perimeter += hypotenuse
    elif x != x_previous and y == y_previous:
        length = abs(x - x_previous)
        perimeter += length
    elif x == x_previous and y != y_previous:
        length = abs(y - y_previous)
        perimeter += length
    else:
        print("Coordinates did not change, enter different coordinates")
