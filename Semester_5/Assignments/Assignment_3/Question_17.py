def remove_vowels(str_):
    result = ''
    for i in range(len(str_)):
        if str_[i] not in 'aeiouAEIOU':
            result += str_[i]
    return result

def remove_vowels2(str_):
    for i in str_:
        if i in 'aeiouAEIOU':
            str_ = str_.replace(i, "")
    return str_

print(remove_vowels('I am a good boy'))
print(remove_vowels2('I am a good boy'))