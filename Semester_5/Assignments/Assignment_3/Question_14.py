def is_armstrong_number(num):
    num_str = str(num)
    power = len(num_str)

    armstrong_sum = sum(int(digit) ** power for digit in num_str)
    return armstrong_sum == num

number = int(input("Enter a number: "))
if is_armstrong_number(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")