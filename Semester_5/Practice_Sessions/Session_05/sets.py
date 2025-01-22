print()
set1 = {5, 3, 1, 8, 8, 2, 7, 'Debadarshi Omkar', True, False, None, (1, 4)} # Set can contain a tuple in it but not list, because set can contain only immutable data
print(type(set1))
print(set1)

set2 = {}  # This is an empty dictionary
print(type(set2))
set2 = set()  # This is an empty set
print(type(set2), '\n')

set2 = {2, 4, 8, 'Guddu', 3, 6}
# Set methods
# len()
print('No. of elements in set1 is:', len(set1), '\n')

# add()
set1.add('Europe')
print('Adding new element set1:', set1, '\n')

# remove() & pop()
value = set1.remove(3)
print('After removal of 3 from set1:', set1)
print('Popped element:', set1.pop())  # pop() randomly deletes an element from set
print('After popping an element from set1:', set1, '\n')

# clear()
# set1.clear() # makes the set an empty set
# print(set1)

# union(), intersection(), difference(), issubset() and issuperset()
print('set1 union set2:', set1.union(set2))
print('set1 intersection set2:', set1.intersection(set2))
print('set1 difference set2:', set1.difference(set2))
print('Is set2 a subset of set1:', set2.issubset(set1))
print('Is set1 a superset of (2, 7, 8):', set1.issuperset({2, 7, 8}), '\n')
