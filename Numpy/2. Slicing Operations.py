import numpy as np
arr_2d = np.array([[10, 20, 30, 40],
                   [50, 60, 70, 80],
                   [90, 100, 110, 120]])

print("Original 2D Array:")
print(arr_2d)
print("--------------------")

# --------------------
# Indexing
# --------------------
# Access a single element
# The syntax is array[row_index, column_index]
element = arr_2d[1, 2] # Accesses the element in the second row (index 1) and third column (index 2)
print("Accessing a single element at [1, 2]:", element)
print("--------------------")

# --------------------
# Slicing
# --------------------
# Slicing extracts a subarray from the original array.
# The syntax is array[start_row:end_row, start_column:end_column]
# Remember that the end index is exclusive.

# Slice a single row
# The colon : selects all columns.
row_slice = arr_2d[0, :]
print("Slicing the first row:")
print(row_slice)
print("--------------------")

# Slice a single column
# The colon : selects all rows.
column_slice = arr_2d[:, 1]
print("Slicing the second column:")
print(column_slice)
print("--------------------")

# Slice a subarray (a sub-matrix)
sub_array = arr_2d[0:2, 1:3] # Rows from index 0 to 1, and columns from index 1 to 2.
print("Slicing a subarray (rows 0-1, columns 1-2):")
print(sub_array)
print("--------------------")

# Slicing with a step
# You can specify a step size to skip elements.
stepped_slice = arr_2d[::2, ::2] # Selects every second row and every second column
print("Slicing with a step of 2:")
print(stepped_slice)
print("--------------------")

# Slicing to get the last row/column
last_row = arr_2d[-1, :]
print("Slicing the last row:")
print(last_row)
print("--------------------")

# Slicing to get the last two columns
last_two_cols = arr_2d[:, -2:]
print("Slicing the last two columns:")
print(last_two_cols)
print("--------------------")