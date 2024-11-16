numbers = [1, 2, 3, 4, 5]
numbers.extend(6, 7, 8)
# we are trying to extend the numbers list by more than 1 element at a time.
# Throws TypeError: list.extend() takes exactly one argument (3 given)