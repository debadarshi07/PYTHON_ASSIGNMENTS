n = int(input("Enter a number: "))
number = n
i, factorial = 1, 1

while n > factorial:
    factorial *= i
    i += 1

if n == factorial: 
    print(f"{number} is a factorial number of {i - 1}")
else :
    print(f"{number} is not a factorial number")