def print_tabular_format(list_):
    for row in list_:
        print('\t'.join(map(str, row)))

list_ = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print_tabular_format(list_)