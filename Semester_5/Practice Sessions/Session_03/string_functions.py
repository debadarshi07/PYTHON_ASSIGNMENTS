name = 'Debadarshi Omkar'

# len()
print('Length:', len(name), '\n')

# endswith()
print('Name ends with "mkar":', name.endswith('mkar'), '\n')

# startswith()
print('Name starts with "Dis":', name.startswith('Dis'), '\n')

# capitalize()
print('Capitalized name:', name.capitalize(), '\n')

# lower() and upper()
print('Lowercase and Uppercase names: ', name.lower(), ',', name.upper(), '\n')

# title()
sentence = 'debadarshi omkar is a good boy'
print('Title:', sentence.title(), '\n')

# strip()
sentence = '             Debadarshi Omkar is a good boy    '
print('Strip:', sentence.strip(), '\n')

# split()
sentence = 'Debadarshi Omkar, is a good, boy'
print('Words:', sentence.split())
print('Words:', sentence.split(","))
print('Words:', sentence.split(",", 1), '\n')

# join()
word1, word2 = 'First ', 'Second '
words = ['Term1 ', 'Term2 ', 'Term3 ']
print('word1.join(word2):', word1.join(word2))
print('word1.join(words):', word1.join(words))
print('"".join(words):', ''.join(words), '\n')

# replace()
print('replacement:', sentence.replace('a good', 'an amazing'))
print('replacement:', sentence.replace('Deb', 'deb'), '\n')

# find() and rfind()
print('Index of first "d":', name.find('d'))
print('Index of first "sh":', name.find('sh'))
print('Index of last "a":', name.rfind('a'), '\n')

# index() and rindex()
print('Index of first "d":', name.index('d'))
print('Index of first "sh":', name.index('sh'))
print('Index of last "a":', name.rindex('a'), '\n')

# count()
print('No. of "a" in name:', name.count('a'), '\n')

# isalpha(), isdigit(), isalnum() and isspace()
str1, str2, str3, str4 = 'Guddu', 'Guddu07', '07', '  '
print('Is str1 alphabetic:', str1.isalpha())
print('Is str1 digit:', str1.isdigit())
print('Is str1 alphanumeric:', str1.isalnum())
print('Is str1 space:', str1.isspace(), '\n')

print('Is str2 alphabetic:', str2.isalpha())
print('Is str2 digit:', str2.isdigit())
print('Is str2 alphanumeric:', str2.isalnum())
print('Is str2 space:', str2.isspace(), '\n')

print('Is str3 alphabetic:', str3.isalpha())
print('Is str3 digit:', str3.isdigit())
print('Is str3 alphanumeric:', str3.isalnum())
print('Is str3 space:', str3.isspace(), '\n')

print('Is str4 alphabetic:', str4.isalpha())
print('Is str4 digit:', str4.isdigit())
print('Is str4 alphanumeric:', str4.isalnum())
print('Is str4 space:', str4.isspace(), '\n')

# swapcase()
print('Swapped case name:', name.swapcase(), '\n')

# zfill()
str1, str2 = 'Guddu', '18'
print('filled upto 8 characters:', str1.zfill(8))
print('filled upto 7 characters:', str2.zfill(7), '\n')

# These are commonly used string functions in python but there are other string functions as well.

# Escape sequence characters
print("I'm \nDebadarshi Omkar.")
print("I'm a \tgood boy.")
print('I love \'Programming\'.')