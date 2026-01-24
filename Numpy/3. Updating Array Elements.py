import numpy as np
arr_2d = np.array([[10, 20, 30],
                   [40, 50, 60],
                   [70, 80, 90]])

# --------------------
# Changing/Updating Elements
# --------------------
# Change a single element
arr_2d[1, 1] = 55
print("\nArray after changing element at [1, 1] to 55:")
print(arr_2d)

# Change a whole row
arr_2d[2, :] = [75, 85, 95]
print("Array after changing the third row:")
print(arr_2d)

# Change a whole column
arr_2d[:, 0] = [15, 45, 75]
print("Array after changing the first column:")
print(arr_2d)

# Change a subarray
arr_2d[0:2, 0:2] = [[11, 22], [33, 44]]
print("Array after changing the top-left subarray:")
print(arr_2d)