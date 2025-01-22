from copy import copy,deepcopy

def modify_list(list_):
    list_[0][0] = 'Shallow'

list_ = [[1, 2, 3], [4, 5, 6]]
list1 = copy(list_)
list2 = deepcopy(list_)

print(f"list_: {list_}")
print(f"list1: {list1}")
print(f"list2: {list2}")

modify_list(list_)

print(f"\nlist_: {list_}")
print(f"list1: {list1}")
print(f"list2: {list2}")