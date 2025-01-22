numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
print(list(filter(lambda x: x % 2 == 0, map(lambda x: x * 2, numbers))))

# map function first maps the new iterator with all the numbers doubled to filter function. Then the filter function checks whether the any number is even or not. Here as every number is being multiplied by 2 so, obviously all numbers will turn to even. Hence, the filter will return the entire iterator as it is what it got from map function before.