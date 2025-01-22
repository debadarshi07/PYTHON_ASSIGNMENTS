def remove_punctuations(str_):
    return ''.join(ch for ch in str_ if ch.isalnum())

str_ = input("Enter a string: ")
print(f"'{str_}' after removing all punctuations is '{remove_punctuations(str_)}'.")