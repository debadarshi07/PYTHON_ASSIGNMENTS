position = input("Enter a position on chess board: ")
row = int(position[1])
column = position[0]

if 0 < row < 9 and column in 'abcdefgh':
    if (ord(column) + row) % 2 == 0 :
        print(f"{column}{row} is a white box.")
    else :
        print(f"{column}{row} is a black box.")
else:
    print("Enter a valid position.")