def shift_string(str_):
    result = ""
    for ch in str_:
        if ch == 'z':
            result += 'a'
        elif ch == 'Z':
            result += 'A'
        else:
            result += chr(ord(ch) + 1)
    return result

str_ = input("Enter string: ")
print(f"'{str_}' after shifting one letter ahead: '{shift_string(str_)}'.")