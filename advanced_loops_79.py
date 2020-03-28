# The greatest common divisor of two positive integers, n and m, is the largest number,
# d, which divides evenly into both n and m. There are several algorithms that can be
# used to solve this problem, including:
# Initialize d to the smaller of m and n.
# While d does not evenly divide m or d does not evenly divide n do
# Decrease the value of d by 1
# Report d as the greatest common divisor of n and m
# Write a program that reads two positive integers from the user and uses this algorithm
# to determine and report their greatest common divisor.

n = int(input("Please enter a number: "))
m = int(input("please enter another number: "))
while n > 0 and m > 0:
    if n > m:
        d = m
    elif m > n:
        d = n
    else:
        print("There isn't a point in entering the same number twice, you know")
    while (n % d != 0) or (m % d != 0):
            d -= 1
    print(f"The greatest common divisor for {n} and {m} is {d}")
    n = int(input("Please enter a number: "))
    m = int(input("please enter another number: "))