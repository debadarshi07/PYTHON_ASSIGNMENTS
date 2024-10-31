def binary_to_decimal(binary):
    decimal, power = 0, 0
    binary = binary[: : -1]
    for digit in binary:
        decimal += int(digit) * 2 ** power
        power += 1
    return decimal

def decimal_to_binary(decimal):
    binary = ""
    if decimal == 0:
        return 0
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    return binary

binary = input("Enter a binary number: ")
print(f"The decimal equivalent of {binary} is {binary_to_decimal(binary)}.")

decimal = int(input("Enter a decimal number: "))
print(f"The binary equivalent of {decimal} is {decimal_to_binary(decimal)}.")