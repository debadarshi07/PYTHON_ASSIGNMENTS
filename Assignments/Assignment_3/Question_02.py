def find_nums():
    nums = []
    for i in range(100, 500):
        if i % 3 == 0 and i % 5 == 0:
            nums.append(i)
    return nums

print(find_nums())