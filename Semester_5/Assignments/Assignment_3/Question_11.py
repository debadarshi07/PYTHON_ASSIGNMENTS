def can_form_palindrome(str_):
    list_of_chars = list(ch.lower() for ch in str_ if ch.isalnum())
    set_of_chars = set(ch.lower() for ch in str_ if ch.isalnum())
    count = 0
    for ch in set_of_chars:
        if list_of_chars.count(ch) % 2 != 0:
            count += 1
        if count > 1:
            return False
    return True


def can_form_palindrome2(str_):
    char_counter = {}
    for ch in str_:
        if ch.isalnum():
            ch = ch.lower()
            char_counter[ch] = char_counter.get(ch, 0) + 1

    odd_counter = 0
    for count  in char_counter.values():
        if count % 2 != 0:
            odd_counter += 1

    return odd_counter <= 1

str_ = input("Enter a string: ")
print(f"'{str_}' can be arranged to form a palindrome : {can_form_palindrome(str_)}")
print(f"'{str_}' can be arranged to form a palindrome : {can_form_palindrome2(str_)}")