def dot_product(a, b):
    return sum(x * y for x, y in zip(a, b))

def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def inverse(matrix):
    n = len(matrix)
    # Create an augmented matrix with the identity matrix
    augmented = [row[:] + [1 if i == j else 0 for j in range(n)] for i, row in enumerate(matrix)]

    # Perform Gaussian elimination
    for i in range(n):
        # Make the diagonal contain all 1s
        diag_value = augmented[i][i]
        if diag_value == 0:
            raise ValueError("Matrix is not invertible.")
        for j in range(2 * n):
            augmented[i][j] /= diag_value

        # Make the other rows contain 0s in the current column
        for k in range(n):
            if k != i:
                factor = augmented[k][i]
                for j in range(2 * n):
                    augmented[k][j] -= factor * augmented[i][j]

    # Extract the inverse matrix from the augmented matrix
    return [row[n:] for row in augmented]

def matrix_multiply(A, B):
    result = []
    for i in range(len(A)):
        result_row = []
        for j in range(len(B[0])):
            result_row.append(dot_product(A[i], [B[k][j] for k in range(len(B))]))
        result.append(result_row)
    return result

def calculate_weights(X, y):
    X_bias = [[1] + list(x) for x in X]
    
    Xt = transpose(X_bias)
    XtX = matrix_multiply(Xt, X_bias)
    XtX_inv = inverse(XtX)
    XtY = matrix_multiply(Xt, [[val] for val in y])
    
    return matrix_multiply(XtX_inv, XtY)

def main():
    
    n = int(input("Enter the number of car records: "))
    
    ages = []
    mileages = []
    prices = []

    for i in range(n):
        price = float(input(f"Enter the price of car {i + 1} (in units of 10k dollars): "))
        
        age = float(input(f"Enter the age of car {i + 1} (in years): "))
        
        mileage = float(input(f"Enter the mileage of car {i + 1} (in thousands of miles): "))
        
        ages.append(age)
        mileages.append(mileage)
        prices.append(price)

    X = list(zip(ages, mileages))
    y = prices

    weights = calculate_weights(X, y)
    print("Calculated weights (coefficients):", [w[0] for w in weights])

    new_age = float(input("Enter the age of the car you want to predict the price for (in years): "))
    new_mileage = float(input("Enter the mileage of the car you want to predict the price for (in thousands of miles): "))
    
    new_X = [1, new_age, new_mileage] 
    predicted_price = dot_product(new_X, [w[0] for w in weights]) 

    print(f"The predicted price for a car aged {new_age} years with {new_mileage}K miles is: ${predicted_price:.2f}")

main()