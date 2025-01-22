list1 = ['Debadarshi', 'Australia', 21.1, False, 7, 'ITER', True, None]
print('First element in list1:', list1[0], '\n')

list1[0] = 'Omkar Debadarshi'  # python lists are mutable
print('Changed index 0:', list1, '\n')

list1[0 : 2] = ['Debadarshi Omkar', 'Germany']
print('Changed index 0 and 1:', list1, '\n')

list2 = list(list1)
print('list2:', list2)
list2[2 : ] = ['Term1']
print('Updated list2:', list2, '\n')

# list traversal
print('Elements in list1:')

#for in
for item in list1:
    print(item, end = ' ')
print()

#for loop
for i in range(len(list1)):
    print(list1[i], end = ' ')
print()

#while loop
i = 0
while i < len(list1):
    print(list1[i], end = ' ')
    i += 1
print()

# short hand for loop
[print(x, end = ' ') for x in list1]
print()
list((print(x, end = ' ') for x in list1))
print()

# unpacking(* operator)
print(*list1, '\n')

print(type(list1))
print('elements in list1 from index 2:', list1[2 : ])
print('elements in list1 from index 0 to 4:', list1[0 : 4], '\n')

print('Final list1:', list1)
print('Final list2:', list2)
print()