# Discount Calculation
cost_price = float(input("Enter the cost price of the item: "))
discount_rate = 20  # in percent
discounted_price = cost_price - (cost_price * discount_rate / 100)

print(f"The total price after a 20% discount is: {discounted_price}")