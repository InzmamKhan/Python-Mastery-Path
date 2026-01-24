import numpy as np
matrix_a = np.array([[4, 7],
                     [2, 6]])
matrix_b = np.array([[1, 2],
                     [3, 4]])

print("Matrix A:")
print(matrix_a)
print("\nMatrix B:")
print(matrix_b)
print("-" * 30)

# 1. Determinant
# The determinant is a scalar value that provides information about the matrix.
# It can be calculated using np.linalg.det()
determinant = np.linalg.det(matrix_a)
print("Determinant of Matrix A:", determinant)
print("-" * 30)

# 2. Inverse
# The inverse of a matrix, when multiplied by the original matrix,
# results in the identity matrix. It's calculated using np.linalg.inv().
try:
    inverse_a = np.linalg.inv(matrix_a)
    print("Inverse of Matrix A:")
    print(inverse_a)
    print("\nVerification (A * A_inv):")
    # Multiplying the matrix by its inverse should give the identity matrix.
    # The result may have very small floating-point errors, so we use np.round().
    print(np.round(np.dot(matrix_a, inverse_a)))
except np.linalg.LinAlgError:
    print("Matrix A is singular and does not have an inverse.")
print("-" * 30)

# 3. Matrix Multiplication (Dot Product)
# This is a true matrix multiplication operation, not element-wise.
# You can use np.dot() or the @ operator.
dot_product = np.dot(matrix_a, matrix_b)
# or
# dot_product = matrix_a @ matrix_b
print("Dot Product of Matrix A and B:")
print(dot_product)
print("-" * 30)

# 4. Transpose
# The transpose of a matrix is obtained by flipping it over its main diagonal.
# Rows become columns and columns become rows.
transpose_a = matrix_a.T
print("Transpose of Matrix A:")
print(transpose_a)
print("-" * 30)