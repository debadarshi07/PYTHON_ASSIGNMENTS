from math import sqrt

limit = int(input("Enter a limit: "))
sum = 0

for num in range (2, limit) :
    count = 0
    for i in range (2 , int(sqrt(num))):
        if num % i == 0:
            count += 1
    if count == 0:
        sum += num

print(f"Sum of all prime numbers less than {limit} is {sum}.")