def is_sorted(list_):
    return list_ == sorted(list_)

user_input = input("Enter list: ")
numbers = list(map(int, user_input.split()))
numbers = numbers[1 : ]

if is_sorted(numbers):
    print("The list is already sorted.")
else:
    print("The list is not sorted.")