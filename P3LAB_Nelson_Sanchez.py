# Nelson Sanchez
# P3LAB
# 03/03/2026
# Description: This program accepts a monetary amount from the user
# and calculates the most efficient number of dollars, quarters,
# dimes, nickels, and pennies needed to make that amount.


# Get user input
amount = float(input("Enter a money value: $"))

# Convert to cents (integer)
total_cents = int(round(amount * 100))

# Calculate dollars
dollars = total_cents // 100
total_cents = total_cents - (dollars * 100)

# Calculate quarters
quarters = total_cents // 25
total_cents = total_cents - (quarters * 25)

# Calculate dimes
dimes = total_cents // 10
total_cents = total_cents - (dimes * 10)

# Calculate nickels
nickels = total_cents // 5
total_cents = total_cents - (nickels * 5)

# Remaining cents are pennies
pennies = total_cents

# Display results
if dollars > 0:
    if dollars == 1:
        print("1 Dollar")
    else:
        print(dollars, "Dollars")

if quarters > 0:
    if quarters == 1:
        print("1 Quarter")
    else:
        print(quarters, "Quarters")

if dimes > 0:
    if dimes == 1:
        print("1 Dime")
    else:
        print(dimes, "Dimes")

if nickels > 0:
    if nickels == 1:
        print("1 Nickel")
    else:
        print(nickels, "Nickels")

if pennies > 0:
    if pennies == 1:
        print("1 Penny")
    else:
        print(pennies, "Pennies")