# The value of π can be approximated by the following infinite series:
# π ≈ 3 +
# 4
# 2 × 3 × 4 − 4
# 4 × 5 × 6 +
# 4
# 6 × 7 × 8 − 4
# 8 × 9 × 10 +
# 4
# 10 × 11 × 12 −···
# Write a program that displays 15 approximations of π. The first approximation should make use of only the first term from the infinite series. Each additional
# approximation displayed by your program should include one more term in the series,
# making it a better approximation of π than any of the approximations displayed previously

PI = 3
x = 2
flag = True
approximation = int(input("How many approximations of π doy want to display? "))
for i in range(approximation):
    if flag:
        PI += 4 / (x * (x + 1) * (x + 2))
        flag = False
    else:
        PI -= 4 / (x * (x + 1) * (x + 2))
        flag = True
    x += 2
print(PI)