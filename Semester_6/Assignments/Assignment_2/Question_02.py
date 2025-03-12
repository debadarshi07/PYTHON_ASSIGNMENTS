def gcd(x, y):
    if x < y:
        return gcd(y, x)
    if (y == 0):
        return x
    return gcd(y, x % y)

print(f'{gcd(10, 150)}')