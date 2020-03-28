# Write a program that converts a binary (base 2) number to decimal (base 10). Your
# program should begin by reading the binary number from the user as a string. Then
# it should compute the equivalent decimal number by processing each digit in the
# binary number. Finally, your program should display the equivalent decimal number
# with an appropriate message
# 10011011 == 155

total = 0
user_string = input("Please enter a binary string: ")
multiplier = len(user_string)
for binary in user_string:
    if binary != "0":
        base = 2 ** (multiplier-1)
        total += base
    multiplier -= 1

print(f"The equivalent decimal number for binary string {user_string} is {total}")

# Write a program that converts a decimal (base 10) number to binary (base 2). Read the
# decimal number from the user as an integer and then use the division algorithm shown
# below to perform the conversion. When the algorithm completes, result contains the
# binary representation of the number. Display the result, along with an appropriate
# message.
# Let result be an empty string
# Let q represent the number to convert
# repeat
# Set r equal to the remainder when q is divided by 2
# Convert r to a string and add it to the beginning of result
# Divide q by 2, discarding any remainder, and store the result back into q
# until q is 0

result = ""
if user_string != "":
    q = total
else:
    q = int(input("Please enter a decimal number to convert: "))
while q != "":
    while q != 0:
        r = q % 2
        result = str(r) + result
        q = q // 2
    print(f"The equivalent binary string for decimal number {q} is {result}")
q = int(input("Please enter a decimal number to convert: "))