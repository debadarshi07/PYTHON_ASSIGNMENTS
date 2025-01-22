def replace_vowels(str_):
    for ch in str_:
        if ch in 'aeiouAEIOU':
            str_ = str_.replace(ch, '*')
    return str_

str_ = input("Enter string: ")
print(f"'{str_}' after replacing all the vowels with '*' : '{replace_vowels(str_)}'")