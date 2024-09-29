for i in range(1, 5):
    print(' ' * (5 - i), end='')
    print('*', end='')
    if i > 1:
        print(' ' * (2 * i - 3), end='')
        print('*', end='')
    print()
print('*' * (2 * 5 - 1))