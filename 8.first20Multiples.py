# Input a number from the user
num = int(input("Enter a number: "))

# Initialize an empty list to store multiples
multiples = []

# Generate the first 20 multiples
for i in range(1, 21):
    multiples.append(num * i)

# Print the multiples
print(f"The first 20 multiples of {num} are:", multiples)