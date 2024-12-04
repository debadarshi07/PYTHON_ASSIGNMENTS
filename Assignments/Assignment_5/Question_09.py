str = 'mississippi'
letter_count = {}

for letter in str:
    letter_count[letter] = letter_count.get(letter, 0) + 1

print(letter_count)