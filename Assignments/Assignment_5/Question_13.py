def alphabetic_order(list_):
    unique = set(key for key in list_)
    list_ = [word for word in unique]
    list_.sort()
    for word in list_:
        print(word, end = ' ')

string_ = input('Enter a sentence: ').lower()
string_ = ''.join([char for char in string_ if char.isalnum() or char.isspace()])

words = string_.split()
alphabetic_order(words)