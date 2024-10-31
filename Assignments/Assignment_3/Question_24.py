from string import punctuation as pun

def remove_punctuations(str_):
    return ''.join(ch for ch in str_ if ch not in pun)

str_ = input("Enter a string: ")
print(f"'{str_}' after removing all punctuations is '{remove_punctuations(str_)}'.")