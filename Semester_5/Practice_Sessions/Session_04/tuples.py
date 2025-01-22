print()
tuple1 = (4)
print(type(tuple1))
tuple2 = (4, )
print(type(tuple2), '\n')

tuple1 = ('Debadarshi', 'Australia', 21.1, False, 7, 'ITER', True, None)
tuple2 = ('Java', 'Python', 'Ruby', 'JS', 'Dart')
print('tuple1:', tuple1, '\n')

print('tuple1[0]:', tuple1[0])
print('tuple1[1 : : 2]', tuple1[1 : : 2])
print('tuple1[2 : 6]:', tuple1[2 : 6], '\n')

if None in tuple1:
    print('"None" is present in tuple1.\n')

tuple1 += tuple2
print('Updated tuple1:', tuple1, '\n')

# tuple1[0] = 'Debadarshi Omkar' # python tuple is immutable
# print('tuple1:', tuple1)

# adding and removing elements in tuple
# tuples are immutable, so we can't add or remove elements from a tuple. But we can convert the tuple to list and update elements.

list1 = list(tuple1)
list1[4] = 'Germany'
list1.insert(2, 'Student')
list1.remove('Australia')
list1.pop(8)
tuple1 = tuple(list1)
print('Type of tuple1 after update:', type(tuple1))
print('Updated tuple1:', tuple1, '\n')

# del keyword
# del tuple1   # tuple1 no longer exits

# unpack tuples
print('tuple2 elements: ')
(dsa, ai, ios, web, android) = tuple2
print(dsa, ai)
for x in (dsa, ai, ios, web, android):
    print(x, end = ' ')
print('\n')

# tuple methods
# len()
print('Length of tuple1:', len(tuple1), '\n')

# max() and min()
print('Max element in tuple2:', max(tuple2))
print('Min element in tuple2:', min(tuple2), '\n')

# count()
print('Frequency of 7 in tuple1:', tuple1.count(7))
print('Frequency of "Ruby" in tuple2:', tuple1.count('Ruby'), '\n')

# index()
print('Index of "JS" in tuple1 is:', tuple1.index('JS'))
print('Index of "Dart" in tuple2 is:', tuple2.index('Dart'), '\n')