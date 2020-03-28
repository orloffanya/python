# Consider a sequence of integers that is constructed in the following manner:
# Start with any positive integer as the only term in the sequence
# While the last term in the sequence is not equal to 1 do
# If the last term is even then
# Add another term to the sequence by dividing the last term by 2 using
# floor division
# Else
# Add another term to the sequence by multiplying the last term by 3 and
# adding 1
# The Collatz conjecture states that this sequence will eventually end with one when
# it begins with any positive integer. Although this conjecture has never been proved,
# it appears to be true.
# Create a program that reads an integer, n, from the user and reports all of the
# values in the sequence starting with n and ending with one. Your program should
# allow the user to continue entering new n values (and your program should continue
# displaying the sequences) until the user enters a value for n that is less than or equal
# to zero.

new = 0
n = int(input("Please enter a number over a zero: "))
while n > 0:
    n = str(n)
    while n[-1] != "1":
        if len(str(new)) < 2:
            if int(n[-1]) % 2 == 0:
                new = int(n[-1]) // 2
                n = n + str(new)
            else:
                new = (int(n[-1]) * 3) + 1
                n = n + str(new)
        else:
            if new % 2 == 0:
                new = new // 2
                n = n + str(new)
            else:
                new = (new * 3) + 1
                n = n + str(new)
    print(n)
    n = int(input("Please enter a number over a zero: "))