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

num = int(input('Enter a number: '))
num_str = ''

while num > 0:
    num_str = f"{digit_to_string[num % 10]} " + num_str
    num = num // 10

print(f"' {num_str}'")