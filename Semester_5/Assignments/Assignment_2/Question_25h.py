for i in range(4):
    print(' ' * (4 - i - 1), end='')
    
    if i == 0:
        print('*')
    else:
        print('*', end='')
        print(' ' * (2 * i - 1), end='')
        print('*')

for i in range(4 - 2, -1, -1):
    print(' ' * (4 - i - 1), end='')
    
    if i == 0:
        print('*')
    else:
        print('*', end='')
        print(' ' * (2 * i - 1), end='')
        print('*')