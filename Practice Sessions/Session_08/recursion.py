print()
# recursive functions

# factorial of a given number
def factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)

# nth fibonacci number
def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
# printing a fibonacci series
def fibonacci_series(n, first = 0, second = 1, count = 0):
    if n <= 0:
        return "Input should be a positive integer."
    if count > n:
        return
    print(first, end = ' ')
    fibonacci_series(n, second, first + second, count + 1)


# calling all the above functions below

# num = int(input("Enter a number: "))
# print(f"Factorial of {num} is: {factorial(num)}")

# n = int(input("Enter n: "))
# print(f"{n}th number in fibonacci series is: {fibonacci(n)}")

# n = int(input("Enter n: "))
# print(f"Fibonacci Series upto {n}th term: ", end = ' ')
# fibonacci_series(n)