# Nelson Sanchez
# 3/11/2026
# P3HW2
# Create a program that calulates the employees pay and hours worked 

# Get user input 
name = input("Eneter employee's name: ")
hours = float(input("Enter number of hours worked: "))
rate = float(input("Enter employees pay rate: "))

print("_" * 40)
print("Employee name:  ",name)
print()

# Overtime calculation using IF/ElSE
if hours > 40:
    overtime_hours = hours -40
    regular_hours = 40
else:
    overtime_hours = 0
    regular_hours = hours

# pay calculations 
regular_pay = regular_hours * rate
overtime_pay = overtime_hours * rate * 1.5
gross_pay = regular_pay + overtime_pay

# Display resultes
print("Hours worked pay Rate Overtime Overtime pay RegHour pay Gross pay")
print("----------------------------------------------------------------")
print(f"{hours:.1f}           {rate:.1f}       {overtime_hours:.1f}       "
      f"{overtime_pay:.2f}        ${regular_pay:.2f}      ${gross_pay:.2f}")