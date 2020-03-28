# Display pi (π) to five decimal places.
# Ask the user to enter the radius of a circle
# (measurement from the centre point to the edge). Work out the area of the circle (π*radius2).
# Ask for the radius and the depth of a cylinder
# and work out the total volume (circle area*depth) rounded to three decimal places.
PI = 3.14159265359
print(round(PI, 5))
radius = int(input("please enter a radius of a circle "))
area = PI * radius ** 2
print(f"the area of the circle is {area}")
depth = int(input("please type the depth of cylinder "))
volume = area * depth
print(f"the cylinder's volume is {round(volume, 3)}")
