# Nelson Sanchez
# 3/29/2026
# P4HW2
# Calculates Pay for multiple employees, and displays the sum of total payment.

#Pseudocode:

# 1. Initialize accumulators for total employees, total regular pay, total overtime pay, and total gross pay.
# 2. Start an input loop to process multiple employees:
#   a. Prompt user for employee's name.
#   b. If the user enters "Done" (case-insensitive), exit the loop.
#   c. Prompt user to enter hours worked.
#   d. Prompt user to enter hourly pay rate.
#   e. Calculate overtime hours (any hours over 40).
#   f. Calculate overtime pay as overtime hours multiplied by 1.5 times the hourly rate.
#   g. Calculate regular hours (maximum 40).
#   h. Calculate regular pay as regular hours multiplied by hourly rate.
#   i. Calculate gross pay as sum of regular pay and overtime pay.
#   j. Update accumulators with employee’s pay amounts and increment employee count.
#   k. Display the individual employee’s pay details in a formatted table.
# 3. After exiting the loop, display the totals for:
#   - Number of employees processed
#   - Total overtime pay
#   - Total regular pay
#   - Total gross pay

def main():
    # Initialize totals and counters
    total_employees = 0
    total_regular_pay = 0.0
    total_overtime_pay = 0.0
    total_gross_pay = 0.0

    while True:
        name = input("Enter employee's name or \"Done\" to terminate: ").strip()
        if name.lower() == "done":
            break  # Exit the loop when sentinel is entered

        # Get hours worked, validate input
        while True:
            try:
                hours = float(input(f"How many hours did {name} work? "))
                if hours < 0:
                    print("Hours worked cannot be negative. Please enter again.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a numeric value for hours worked.")

        # Get pay rate, validate input
        while True:
            try:
                pay_rate = float(input(f"What is {name}'s pay rate? "))
                if pay_rate < 0:
                    print("Pay rate cannot be negative. Please enter again.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a numeric value for pay rate.")

        # Calculate overtime and regular hours
        overtime_hours = max(0, hours - 40)
        regular_hours = min(40, hours)

        # Calculate pays
        overtime_pay = overtime_hours * pay_rate * 1.5
        regular_pay = regular_hours * pay_rate
        gross_pay = regular_pay + overtime_pay

        # Update totals
        total_employees += 1
        total_regular_pay += regular_pay
        total_overtime_pay += overtime_pay
        total_gross_pay += gross_pay

        # Display employee pay summary
        print(f"\nEmployee name:  {name}\n")
        print(f"{'Hours Worked':<13} {'Pay Rate':<9} {'Overtime':<9} {'Overtime Pay':<13} {'RegHour Pay':<12} {'Gross Pay':<10}")
        print("-" * 80)
        print(f"{hours:<13.1f} {pay_rate:<9.2f} {overtime_hours:<9.1f} {overtime_pay:<13.2f} ${regular_pay:<11.2f} ${gross_pay:<9.2f}\n")

    # After all employees processed, show totals
    print(f"Total number of employees entered: {total_employees}")
    print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
    print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
    print(f"Total amount paid in gross: ${total_gross_pay:.2f}")

if __name__ == "__main__":
    main()