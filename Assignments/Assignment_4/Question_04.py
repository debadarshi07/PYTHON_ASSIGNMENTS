def remove_occurrences(list_, element):
    while element in list_:
        list_.remove(element)
    return list_

_list = [2, 1, 5, 4, 3, 8, 3, 7, 3, 2, 3]
element = 3

remove_occurrences(_list, element)
print(f"Modified list: {_list}")
print(len(_list))