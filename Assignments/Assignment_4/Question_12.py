def input_matrix(m, n):
    matrix_ = [[int(input(f"Enter element [{i}][{j}]: ")) for j in range(n)] for i in range(m)]
    return matrix_

def sum_of_column (matrix_, column):
    return sum(matrix_[i][column - 1] for i in range(len(matrix_)))

m, n = int(input("Enter no. of rows: ")), int(input("Enter no. of columns: "))
matrix_ = input_matrix(m, n)

column_to_sum = int(input("Enter the column sum: "))
print(f"{sum_of_column(matrix_, column_to_sum)}")