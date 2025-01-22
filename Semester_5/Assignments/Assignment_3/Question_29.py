def is_perfect_number(num):
    if num <= 0:
        return False
    sum = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            sum += i
    return num == sum

num = int(input("Enter a number: "))
print(f"{num} is a perfect number: {is_perfect_number(num)}")