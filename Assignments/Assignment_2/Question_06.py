from math import sqrt

num = int(input("Enter a number: "))
if num == 1 or num == 0 :
    print(f"{num} is a special number")
    exit()
    
count = 0
for i in range (2 , int(sqrt(num))):
    if num % i == 0 :
        count += 1

if count > 0 :
    print(f"{num} is not a prime number.")
else :
    print(f"{num} is a prime number.")