import numpy as np
arr_2d = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]])

print("Original 2D Array:")
print(arr_2d)
print("-" * 30)






# --------------------
# 1. Reshaping
# --------------------
# Reshape the array into a different shape, but with the same number of elements.
# The original array has 3 rows and 4 columns (12 elements).
# We can reshape it into a 4x3 array, a 6x2 array, etc.

# Reshape to 4 rows and 3 columns
reshaped_arr = arr_2d.reshape(4, 3)
print("Reshaped Array (4x3):")
print(reshaped_arr)
print("-" * 30)

# Reshape to a 1D array (flattening)
# The -1 argument automatically calculates the required dimension.
flattened_arr = arr_2d.reshape(-1)
print("Flattened Array (1D):")
print(flattened_arr)
print("-" * 30)






# --------------------
# 2. Transposing (a form of Reorganizing)
# --------------------
# Transpose flips the array over its main diagonal, converting rows to columns and vice-versa.
transposed_arr = arr_2d.T
print("Transposed Array:")
print(transposed_arr)
print("-" * 30)







# --------------------
# 3. Stacking
# --------------------
# Stacking joins arrays along a new axis.

# Create another 2D array for stacking
arr_b = np.array([[13, 14, 15, 16],
                  [17, 18, 19, 20]])

print("Array to be stacked (arr_b):")
print(arr_b)
print("-" * 30)

# Vertical Stacking (joining row-wise) using np.vstack()
# Arrays must have the same number of columns.
v_stacked_arr = np.vstack((arr_2d, arr_b))
print("Vertically Stacked Array (np.vstack):")
print(v_stacked_arr)
print("-" * 30)

# Horizontal Stacking (joining column-wise) using np.hstack()
# Arrays must have the same number of rows.
# We first need to transpose arr_b so it has 3 rows.
arr_b_transposed = arr_b.T
h_stacked_arr = np.hstack((arr_2d, arr_b_transposed))
print("Horizontally Stacked Array (np.hstack):")
print(h_stacked_arr)
print("-" * 30)