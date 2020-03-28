# February 4, 2013 was the last day that pennies were distributed by the Royal Canadian
# Mint. Now that pennies have been phased out retailers must adjust totals so that they
# are multiples of 5 cents when they are paid for with cash (credit card and debit card
# transactions continue to be charged to the penny). While retailers have some freedom
# in how they do this, most choose to round to the closest nickel.
# Write a program that reads prices from the user until a blank line is entered.
# Display the total cost of all the entered items on one line, followed by the amount
# due if the customer pays with cash on a second line. The amount due for a cash
# payment should be rounded to the nearest nickel. One way to compute the cash
# payment amount is to begin by determining how many pennies would be needed to
# pay the total. Then compute the remainder when this number of pennies is divided
# by 5. Finally, adjust the total down if the remainder is less than 2.5. Otherwise adjust
# the total up.

total = 0
print("Let's shop...")
exact_price = input("Please enter the price: ")
while exact_price == "":
    print("It's too early to quit, we haven't even started yet")
    exact_price = input("Please enter the price: ")
while exact_price != " ":
    total += float(exact_price)
    # print(total)
    exact_price = input("Please enter the price: ")
pennies = (total * 100) % 5
# print(pennies)
if pennies > 2.5:
    nickels = total - (pennies / 100) + 0.05
    # print(f"{total} - ({pennies} / 100) + 0.05 = {nickels}")
else:
    nickels = total - (pennies / 100)
    # print(f"{nickels} = {total} - ({pennies} / 100)")
print(f"The exact price is {round(total, 2)}\nIf you pay by cash it is {round(nickels, 2)}")
