count = 0
for i in range(100, 1000) :
    if count == 10 :
        print()
        count = 0
    if i % 5 == 0 or i % 6 == 0 :
        print(i, end = ' ')
        count += 1