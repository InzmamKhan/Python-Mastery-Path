import numpy as np
arr_2d = np.array([[10, 20, 30],
                   [4, 5, 6],
                   [70, 80, 9]])

print("Original 2D Array:")
print(arr_2d)

# 1. Create a boolean mask
# The mask is a 2D array of True/False values with the same shape as arr_2d.
# True values correspond to elements that meet the condition.
# Here, we create a mask for all elements greater than 10.
mask = arr_2d > 10
print("\nBoolean Mask (arr_2d > 10):")
print(mask)

# 2. Apply the mask to the array
# This operation returns a new 1D array containing only the elements where the mask is True.
masked_elements = arr_2d[mask]
print("\nElements extracted using the mask:")
print(masked_elements)