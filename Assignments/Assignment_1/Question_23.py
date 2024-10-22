num = int(input("Enter a number: "))

last_digit = num % 10
digits_in_number = str(last_digit) + " "
sum = last_digit
num //= 10

while (num > 0) :
    digit = num % 10
    digits_in_number = str(digit) + " + " + digits_in_number
    sum += digit
    num //= 10

print(f"{digits_in_number} = {sum}")