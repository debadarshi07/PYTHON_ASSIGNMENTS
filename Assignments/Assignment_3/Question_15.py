def nth_fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        first, second = 0, 1
        for _ in range(2, n):
            first, second = second, first + second
        return second
        
n = int(input("Enter n: "))
print(nth_fibonacci(n))