import numpy as np
arr1 = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

arr2 = np.array([[9, 8, 7],
                 [6, 5, 4],
                 [3, 2, 1]])

print("Array 1:")
print(arr1)
print("\nArray 2:")
print(arr2)
print("--------------------")





# --- Arithmetic Operations ---

# Addition
addition_result = arr1 + arr2
# This adds the elements at the same position in both arrays.
print("Addition (arr1 + arr2):")
print(addition_result)
print("--------------------")

# Subtraction
subtraction_result = arr1 - arr2
# This subtracts the elements of arr2 from the corresponding elements of arr1.
print("Subtraction (arr1 - arr2):")
print(subtraction_result)
print("--------------------")

# Multiplication
multiplication_result = arr1 * arr2
# This is element-wise multiplication, not matrix multiplication.
print("Element-wise Multiplication (arr1 * arr2):")
print(multiplication_result)
print("--------------------")

# Division
division_result = arr1 / arr2
# This performs element-wise division.
print("Element-wise Division (arr1 / arr2):")
print(division_result)
print("--------------------")

# Exponentiation
exponent_result = arr1 ** 2
# This squares each element in arr1.
print("Exponentiation (arr1 ** 2):")
print(exponent_result)
print("--------------------")

# Scalar Operations
# You can also perform arithmetic operations with a single number (a scalar).
scalar_addition = arr1 + 10
print("Scalar Addition (arr1 + 10):")
print(scalar_addition)
print("--------------------")