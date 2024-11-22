# Input a number from the user
num = int(input("Enter a number: "))

# Initialize lists to store odd and even factors
odd_factors = []
even_factors = []

# Find factors and classify them as odd or even
for i in range(1, num + 1):
    if num % i == 0:
        if i % 2 == 0:
            even_factors.append(i)
        else:
            odd_factors.append(i)

# Print the results
print("Odd factors:", odd_factors)
print("Even factors:", even_factors)