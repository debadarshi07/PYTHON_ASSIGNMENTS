number = int(input("Enter a number: "))
sum = 0

while number > 0 :
    sum += number % 10
    number = number // 10
    if number == 0 and sum > 9:
        number = sum
        sum = 0
print(f"The single digit sum is: {sum}")