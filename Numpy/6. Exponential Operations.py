import numpy as np
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print("Original 2D Array:")
print(arr_2d)
print("-" * 30)

# 1. Logarithmic Operations
# Natural logarithm (base e)
log_natural = np.log(arr_2d)
print("Natural Logarithm (np.log):")
print(log_natural)
print("-" * 30)

# Logarithm with base 2
log_base2 = np.log2(arr_2d)
print("Logarithm with Base 2 (np.log2):")
print(log_base2)
print("-" * 30)

# Logarithm with base 10
log_base10 = np.log10(arr_2d)
print("Logarithm with Base 10 (np.log10):")
print(log_base10)
print("-" * 30)

# 2. Exponential Operations
# Exponential function (e^x)
# This calculates e to the power of each element in the array.
exp_e = np.exp(arr_2d)
print("Exponential (np.exp):")
print(exp_e)
print("-" * 30)

# Power operation (e.g., 2^x)
# This calculates 2 to the power of each element.
power_of_2 = np.power(2, arr_2d)
print("Power of 2 (np.power):")
print(power_of_2)
print("-" * 30)