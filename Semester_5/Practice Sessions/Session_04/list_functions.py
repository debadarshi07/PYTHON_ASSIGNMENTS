list1 = ['Debadarshi', 'Australia', 21.1, False, 7, 'ITER', True, None]

#len()
print('No. of elements list1 has:', len(list1), '\n')

# append() & insert()
print('append returned:', list1.append('Student'))
print('appended list1:', list1)
print('insert returned:', list1.insert(3, 9999))
print('After insertion list1:', list1, '\n')

# extend()
terms = ['Term0', 'Term1', 'Term2', 'Term3', 'Term4', 'Term5', 'Term6', 'Term7']
langs = ('Java', 'Python', 'CSS', 'JS', 'C', 'Dart') # this is a tuple

# We can extend a list1 with any iterable be it another list1 or tuple
print('extend returned:', list1.extend(terms))
print('Extending terms:', list1)
print('extend returned:', list1.extend(langs))
print('Extending langs:', list1, '\n')

# remove() and pop()
print('remove returned:', terms.remove("Term4"))
print('Removing "Term4" terms:', terms)
print('pop returned:', terms.pop(4))
print('Popping 5th element terms:', terms, '\n')

# del keyword
# del terms[0]  # deletes the 0th index
# del terms  # deletes the entire 'terms' list1

# clear()
print('clear returned:', terms.clear()) # terms becomes an empty list1
print('After clearing terms:', terms, '\n')

# sort()
nums = [4, 5, 2, 1, 3]
strings = ['pineapple', 'banana', 'apple', 'orange', 'grapes', 'strawberry']
alpha_num = ['banana', 5, 2, 'apple', 'grapes', 4]

print('sort returned:', nums.sort())
print('Sorted nums ascending:', *nums)
print('sort returned:', strings.sort())
print('Sorted strings ascending:', *strings, '\n')
# alpha_num.sort() # string and integer can't be compared
# print('Sorted alpha_num ascending:', *alpha_num, '\n')

print('sort returned:', nums.sort(reverse = True))
print('Sorted nums descending:', *nums)
print('sort returned:', strings.sort(reverse = True))
print('Sorted strings descending:', *strings, '\n')
# alpha_num.sort(reverse = True) # string and integer can't be compared
# print('Sorted alpha_num descending:', *alpha_num, '\n')

# reverse()
print('reverse returned:', nums.reverse())
print('Reversed nums:', *nums)
print('reverse returned:', strings.reverse())
print('Reversed strings:', *strings, '\n')

# list1() and copy()
# both the functions are used to perform deep copy in list1s
nums1 = list(nums)
print('copy returned:', nums.copy())
print(nums1)

strings1 = strings.copy()
print('copy returned:', strings.copy())
print(strings1, '\n')