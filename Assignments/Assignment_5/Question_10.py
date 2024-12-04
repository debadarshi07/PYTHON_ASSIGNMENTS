str = input('Enter a string: ').lower()

vowels = 'aeiou'
vowel_count = {}

for letter in str:
    if letter in vowels:
        vowel_count[letter] = vowel_count.get(letter, 0) + 1

print("Vowels found:", list(vowel_count.keys()))
print("Vowel counts:", vowel_count)