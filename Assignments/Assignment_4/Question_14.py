def generate_tuple():
    return tuple(num ** 2 for num in range(1, 11))

print(generate_tuple())