for x in range(1, 11):
    print(f"{x}: " + ("\U0001f600" * x))

center = " "
number = int(input("Enter a number: "))
i = number
for x in range(1, number + 1):
    i -= 1
    print((center * i) + ("\U0001f600" * x) + (center * i))