def is_vowel(character):
    return character in 'aeiouAEIOU'

character = input("Enter a character: ")
if is_vowel(character):
    print(f"{character} is a vowel.")
else:
    print(f"{character} is a consonant.")