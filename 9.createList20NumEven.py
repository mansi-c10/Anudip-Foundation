# Initialize an empty list to store numbers
numbers = []

# Input 20 numbers from the user
print("Enter 20 numbers:")
for _ in range(20):
    num = int(input("Enter a number: "))
    numbers.append(num)

# Initialize a list to store even numbers
even_numbers = []

# Loop through the list to find even numbers
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

# Print the even numbers
print("Even numbers from the list:", even_numbers)