# Simple Interest Calculation
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in %): "))
time = float(input("Enter the time (in years): "))

simple_interest = (principal * rate * time) / 100
print(f"The simple interest is: {simple_interest}")