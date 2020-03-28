print(f"1) Square \n2) Triangle")
number = int(input("Enter a number: "))
if number == 1:
    sides = int(input("Please enter the length of one of the sides "))
    area = sides**2
    print(f"the area of the square is {area}")
elif number == 2:
    base = int(input("Please enter the base of the triangle "))
    height = int(input("Please enter the height of the triangle "))
    area = base * height
    print(f"the area of the triangle is {area}")
else:
    print("your input is invalid ")