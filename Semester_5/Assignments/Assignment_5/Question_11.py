def convert_to_text(num):
    digit_to_string = {
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five',
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine'
    }
    text_num = ''

    while num > 0:
        text_num = f"{digit_to_string[num % 10]} " + text_num
        num = num // 10

    return text_num

print(convert_to_text(1234))