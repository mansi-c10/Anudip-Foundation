# Input a number from the user
num = int(input("Enter a number: "))

# Initialize an empty list to store factors
factors = []

# Loop to find factors
for i in range(1, num + 1):
    if num % i == 0:
        factors.append(i)

# Print the factors
print(f"The factors of {num} are:", factors)