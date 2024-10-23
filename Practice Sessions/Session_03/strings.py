name = 'Debadarshi Omkar'
print('Full name:', name)

print(name[0], name[1], name[2]) # chracters of python string can be accessed like elements of list.

# python strings are iterable
for ch in name:
    print(ch, end = ' ')

print()

first_name = name[0 : 10]
print('First name:', first_name)

last_name = name[-5 : ]
print('Last name:', last_name)

skip_name = name[0 : 10 : 2]  # third argument is jump amount(here it's 2)
print('Skip name:', skip_name)

name[0] = 'd'
print(name) # throws error because python strings are immutable