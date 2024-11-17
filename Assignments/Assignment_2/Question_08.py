num = int(input("Enter a number: "))
while num < 0:
    num = int(input("Enter a number: "))

print(num * 2) if num % 2 == 0 else print(num ** 2)