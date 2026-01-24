import numpy as np

# 1D Array (Vector)
# This is a one-dimensional array, like a single row of numbers.
arr_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:")
print(arr_1d)
print("Shape:", arr_1d.shape)
print("Dimensions:", arr_1d.ndim)
print("--------------------")

# 2D Array (Matrix)
# This is a two-dimensional array, like a grid or table with rows and columns.
# It's created using a list of lists.
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("2D Array:")
print(arr_2d)
print("Shape:", arr_2d.shape)
print("Dimensions:", arr_2d.ndim)
print("--------------------")

# 3D Array (Tensor)
# This is a three-dimensional array, a cube-like structure with multiple 2D arrays stacked on top of each other.
# It's created using a list of lists of lists.
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("3D Array:")
print(arr_3d)
print("Shape:", arr_3d.shape)
print("Dimensions:", arr_3d.ndim)
print("--------------------")

# ---- Loading Data from Files ----

file_path = 'C:\\Users\\khani\\OneDrive\\Desktop\\Practice Code\\PYTHON\\Mathematical Stuff\\Numpy\\Source File - Numpy.txt'

# Method 1: Using np.loadtxt()
# This is simpler but less flexible. It's good for clean, consistent data.
# The `delimiter` parameter specifies how the values are separated.
data_loadtxt = np.loadtxt(file_path, delimiter=',')
print("Data read using np.loadtxt():")
print(data_loadtxt)
print("\nShape of the array:", data_loadtxt.shape)

print("\n" + "="*40 + "\n")

# Method 2: Using np.genfromtxt()
# This is a more robust function that handles comments, headers, and missing values.
# `skip_header` tells it to ignore the first line.
# `delimiter` is the same as above.
data_genfromtxt = np.genfromtxt(file_path, delimiter=',', comments='#')
print("Data read using np.genfromtxt():")
print(data_genfromtxt)
print("\nShape of the array:", data_genfromtxt.shape)