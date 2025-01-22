def analyze_sets(list1, list2):
    set1 = set(list1)
    set2 = set(list2)

    symmetric_diff = set1 ^ set2
    modified_elements = []

    for element in symmetric_diff:
        if element % 2 == 0:
            modified_elements.append(element * 2)
        else:
            modified_elements.append(element + 5)

    return sorted(modified_elements)

print(analyze_sets([3, 44, 2, 8, 7], [9, 1, 7, 44]))