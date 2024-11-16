address = 'B-6, Lodhi road, Delhi'
list1 = [1, 2, 3]
list2 = ['a', 1, 'z', 26, 'd', 4]
tuple1 = ('a', 'e', 'i', 'o', 'u')
tuple2 = ([2,4,6,8], [3,6,9], [4,8], 5)
#list1[3] = 4   #list1 has size 3 show 3rd index can't be changed
print(list1 * 2)
#print(min(list2))   #int and str can't be compared
print(max(list1))
print(list(address))
list2.extend(['e', 5])
print(list2)
list2.append(['e', 5])
print(list2)
names = ['rohan', 'mohan', 'gita']
names.sort(key= len)
print(names)
list3 = [(x * 2) for x in range(1, 11)]
print(list3)
del list3[1:]
print(list3)
list4 = [ x + y for x in range(1,5) for y in range(1,5)]
print(list4)
#tuple2[3] = 6   #tuple is immutable
#tuple2.append(5)   #tuple is immutable
print(tuple2)
#t1 = tuple2 + (5)   #tuple can only be concatenated with tuple
print(' , ' .join(tuple1))
print(list(zip(['apple', 'orange'], ('red','orange'))))