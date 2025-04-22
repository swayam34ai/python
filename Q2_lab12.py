class Matrix:
    def __init__(self, values):
        # Initialize the matrix with a 3x3 list of lists
        self.values = values
        
    # Matrix Addition
    def __add__(self, other):
        result = []
        for i in range(3):
            row = []
            for j in range(3):
                row.append(self.values[i][j] + other.values[i][j])
            result.append(row)
        return Matrix(result)

    # Matrix Multiplication
    def __mul__(self, other):
        result = []
        for i in range(3):
            row = []
            for j in range(3):
                sum = 0
                for k in range(3):
                    sum += self.values[i][k] * other.values[k][j]
                row.append(sum)
            result.append(row)
        return Matrix(result)

    # Matrix Transpose
    def transpose(self):
        result = []
        for i in range(3):
            row = []
            for j in range(3):
                row.append(self.values[j][i])
            result.append(row)
        return Matrix(result)

# Creating two 3x3 matrices
matrix1 = Matrix([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

matrix2 = Matrix([
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
])

# Matrix addition
add_result = matrix1 + matrix2

# Matrix multiplication
mul_result = matrix1 * matrix2

# Matrix transpose
transpose_result = matrix1.transpose()

# Display results
print("Matrix 1:")
print(matrix1)
print("Matrix 2:")
print(matrix2)

print("Matrix Addition Result:")
print(add_result)

print("Matrix Multiplication Result:")
print(mul_result)

print("Matrix 1 Transpose Result:")
print(transpose_result)
