# Nelson Sanchez
# 4/19/2025
# P5LAB
# Calculates change and breaks down change in exact bills and coins. 

def disperse_change(change):
    # Convert to cents to avoid floating point issues
    cents = int(round(change * 100))

    dollars = cents // 100
    cents %= 100

    quarters = cents // 25
    cents %= 25

    dimes = cents // 10
    cents %= 10

    nickels = cents // 5
    cents %= 5

    pennies = cents

    # Display results
    if dollars > 0:
        print(f"{dollars} Dollar{'s' if dollars != 1 else ''}")
    if quarters > 0:
        print(f"{quarters} Quarter{'s' if quarters != 1 else ''}")
    if dimes > 0:
        print(f"{dimes} Dime{'s' if dimes != 1 else ''}")
    if nickels > 0:
        print(f"{nickels} Nickel{'s' if nickels != 1 else ''}")
    if pennies > 0:
        print(f"{pennies} Penn{'ies' if pennies != 1 else 'y'}")


def main():
    amount_owed = float(input("You owe $"))
    cash_paid = float(input("How much cash will you put in the self-checkout? "))

    change = round(cash_paid - amount_owed, 2)

    if change < 0:
        print("Insufficient payment.")
    else:
        print(f"Change is: ${change:.2f}\n")
        disperse_change(change)


if __name__ == "__main__":
    main()