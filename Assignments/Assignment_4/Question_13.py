def sort_by_second_element(tuples_list):
    return sorted(tuples_list, key = lambda x: x[1])

tuples = [(1, 4, 3), (3, 2, 5), (1, 5, 1), (4, 3, 11)]
sorted_tuples = sort_by_second_element(tuples)
print(sorted_tuples)