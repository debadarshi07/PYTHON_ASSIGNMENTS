def find_greatest_digits(num):
    greatest, second_greatest, third_greatest = 0, 0, 0
    if len(num) < 2:
        greatest = num
    elif len(num) < 3:
        greatest = max(int(num[0]), int(num[1]))
        second_greatest = min(int(num[0]), int(num[1]))
    else:
        greatest, second_greatest, third_greatest = num[0], num[1], num[2]
        for i in num:
            if (int(i) > int(greatest)):
                third_greatest = second_greatest
                second_greatest = greatest
                greatest = i
    return [greatest, second_greatest, third_greatest]

num = input("Enter a number: ")
print(find_greatest_digits(num))