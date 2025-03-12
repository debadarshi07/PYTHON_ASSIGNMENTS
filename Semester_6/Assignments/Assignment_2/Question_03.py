def print_increasing(n, current_num=0, last_digit=0):
    if n == 0:
        print(current_num)
        return
    for digit in range(last_digit + 1, 10):
        print_increasing(n - 1, current_num * 10 + digit, digit)

n = int(input('Enter n: '))
print_increasing(n)