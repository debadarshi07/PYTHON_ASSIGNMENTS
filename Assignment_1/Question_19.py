cost = float(input("Enter the cost of a meal: "))

tax = cost * 0.15
tip = cost * 0.18

print(f"Tax amount: {tax:.2f}")
print(f"Tip amount: {tip:.2f}")

print(f"Total amount: {(cost + tax + tip):.2f}")