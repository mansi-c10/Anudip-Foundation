# Input a number
number = int(input("Enter a number: "))

# Find the factors
factors = [i for i in range(1, number + 1) if number % i == 0]

# Separate odd and even factors
even_factors = [factor for factor in factors if factor % 2 == 0]
odd_factors = [factor for factor in factors if factor % 2 != 0]

# Print odd and even factors
print("Odd factors:", odd_factors)
print("Even factors:", even_factors)