string = input("Enter a string: ")
length = len(string)

for i in range(length):
    for j in range(i + 1, length + 1):
        print(string[i:j], end = ' ')