char = ord('A')

for i in range(7):
    for j in range(i + 1):
        print(chr(char), end = '')
        char += 1
    print()