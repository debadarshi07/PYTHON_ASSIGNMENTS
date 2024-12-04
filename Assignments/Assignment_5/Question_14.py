string_ = input('Enter a string: ')

# Using set
unique = set(char for char in string_)
print('No. of unique characters:', len(unique))

# Using dictionary
chars = {}
for char in string_:
    chars[char] = chars.get(char, 0) + 1

print('No. of unique characters:', len(chars))