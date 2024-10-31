def number_of_digits(num):
    digit_counter = 0
    while(num > 0):
        digit_counter += 1
        num //= 10
    return digit_counter

num = int(input("Enter the number: "))
print(number_of_digits(num))