import numpy as np
arr_2d = np.array([[10, 20, 5],
                   [30, 4, 15],
                   [25, 8, 3]])

print("Original 2D Array:")
print(arr_2d)
print("-" * 30)

# --- Statistical Operations ---

# 1. Minimum and Maximum
# Find the minimum and maximum values in the entire array
min_value = np.min(arr_2d)
max_value = np.max(arr_2d)
print(f"Minimum value in the array: {min_value}")
print(f"Maximum value in the array: {max_value}")
print("-" * 30)

# 2. Mean, Median, and Standard Deviation
# These are measures of central tendency and dispersion.
mean_value = np.mean(arr_2d)
median_value = np.median(arr_2d)
std_dev = np.std(arr_2d)
print(f"Mean (average) of all elements: {mean_value}")
print(f"Median of all elements: {median_value}")
print(f"Standard Deviation of all elements: {std_dev}")
print("-" * 30)

# 3. Sum of all elements
sum_value = np.sum(arr_2d)
print(f"Sum of all elements: {sum_value}")
print("-" * 30)

# 4. Operations along a specific axis
# You can perform these operations along rows (axis=1) or columns (axis=0).
# Axis 0 refers to the columns, and axis 1 refers to the rows.

# Minimum value of each column
min_per_column = np.min(arr_2d, axis=0)
print("Minimum value of each column:", min_per_column)

# Maximum value of each row
max_per_row = np.max(arr_2d, axis=1)
print("Maximum value of each row:", max_per_row)

# Mean of each column
mean_per_column = np.mean(arr_2d, axis=0)
print("Mean of each column:", mean_per_column)

# Sum of each row
sum_per_row = np.sum(arr_2d, axis=1)
print("Sum of each row:", sum_per_row)