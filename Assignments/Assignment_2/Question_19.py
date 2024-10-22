num = int(input("Enter a number: "))
num2 = num
reverse = 0
while num > 0:
    reverse = reverse * 10 + num % 10
    num //= 10

print(f"Reverse of {num2} is: {reverse}")