# Check if three sides form a triangle
a = float(input("Enter the length of the first side: "))
b = float(input("Enter the length of the second side: "))
c = float(input("Enter the length of the third side: "))

if a + b > c and a + c > b and b + c > a:
    print("The given sides form a triangle.")
else:
    print("The given sides do not form a triangle.")