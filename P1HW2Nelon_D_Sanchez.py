# Nelson Sanchez
# 2/13/2026
# P1hw2
# Travel expense calculator


print("This program calculates and displays travel expenses")

#user inputs own travel expense
print()
budget = int(input("Enter budget: "))
destination = (input("Enter your travel destination: "))
gas = int(input("How much do you think you will spend on gas? "))
hotel = int(input("Approximately, how much will you need for accomodation/hotel?"))
food = int(input("Last, how much do you need for food? "))

#Header of all expenses
print()
print("-------Travel Expenses-------")

#output of location and initial budget
print(f"Location: {destination}")
print(f"initial Budget: {budget}")

#output of total number of each expense
print()
print(f"Fuel: {gas}")
print(f"Accomodation: {hotel}")
print(f"Food: {food}")

#output of the remaning balance after calculations
print(f"Remaining Balance: {budget-gas-hotel-food}")