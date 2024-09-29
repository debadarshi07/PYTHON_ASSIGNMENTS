char = ord('A')

for i in range(8):
    for j in range(i):
        print(chr(char), end = '')
        char += 1
    print()