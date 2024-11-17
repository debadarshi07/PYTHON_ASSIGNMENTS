from random import randint as ri

def generate_matrix():
    return [[ri(0, 1) for i in range(4)] for i in range(4)]

def find_max_ones(matrix_):
    row_max, col_max = 0, 0
    max_row_index, max_col_index = -1, -1

    for index, row in enumerate(matrix_):
        one_count = row.count(1)
        if one_count > row_max:
            row_max = one_count
            max_row_index = index

    for col_index in range(4):
        one_count = sum(matrix_[row_index][col_index] for row_index in range(4))
        if one_count > col_max:
            col_max = one_count
            max_col_index = col_index

    return max_row_index, max_col_index

matrix_ = generate_matrix()
print(matrix_)
print(find_max_ones(matrix_))