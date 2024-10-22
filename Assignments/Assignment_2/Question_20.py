number = int(input("Enter a number: "))
factor = 2
factors = []
i = 0
while number > 1 :
    while number % factor == 0 :
        factors.append(factor)
        i += 1
        number //= factor
    factor += 1

print(f"Factors: {", ".join(map(str,factors))}")