def find_gcd(num1, num2):
    max_, min_ = max(num1, num2), min(num1, num2)
    while min_ != 0:
        max_, min_ = min_, max_ % min_
    return max_

num1, num2 = int(input("Enter first number: ")), int(input("Enter second number: "))
print(f"GCD of {num1} and {num2} is {find_gcd(num1, num2)}.")