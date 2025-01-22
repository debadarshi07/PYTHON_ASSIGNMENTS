def convert_to_text(num):
    digit_text = {
        1 : "one",
        2 : "two",
        3 : "three",
        4 : "four",
        5 : "five",
        6 : "six",
        7 : "seven",
        8 : "eight",
        9 : "nine",
        0 : "zero"
    }
    str_num = str(num)
    text_num = ""
    for ch in str_num:
        text_num += digit_text[int(ch)] + " "
    return text_num

num = int(input("Enter a number: "))
print(f"{num} --> {convert_to_text(num)}")