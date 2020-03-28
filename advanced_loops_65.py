# Write a program that displays a temperature conversion table for degrees Celsius and
# degrees Fahrenheit. The table should include rows for all temperatures between 0
# and 100 degrees Celsius that are multiples of 10 degrees Celsius. Include appropriate
# headings on your columns. The formula for converting between degrees Celsius and
# degrees Fahrenheit can be found on the Internet.

import fractions
i = 10
center = " "
print(f"Celsius{center * i}Fahrenheit{center * i}")
i = 20
for celsius in range(0, 101, 10):
    fahrenheit = celsius * fractions.Fraction(9, 5) + 32
    print(f"{celsius}{center * i}{fahrenheit}{center * i}")
