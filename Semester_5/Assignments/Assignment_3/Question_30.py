def product_of_digits(num):
    if num == 0:
        return 0
    product = 1
    while num > 0:
        product *= num % 10
        num //= 10
    return product

num = int(input("Enter a number: "))
print(f"Product of digits of {num}: {product_of_digits(num)}")