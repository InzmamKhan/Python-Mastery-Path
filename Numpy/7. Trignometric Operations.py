import numpy as np
angles_in_degrees = np.array([[0, 30, 45],
                              [60, 90, 180]])

# --- Trignometric Operations ---


# Convert degrees to radians
angles_in_radians = np.radians(angles_in_degrees)

print("Original 2D Array (in radians):")
print(angles_in_radians)
print("-" * 30)

# 1. Sine Operation
# Calculates the sine of each element.
sine_values = np.sin(angles_in_radians)
print("Sine of each element:")
print(sine_values)
print("-" * 30)

# 2. Cosine Operation
# Calculates the cosine of each element.
cosine_values = np.cos(angles_in_radians)
print("Cosine of each element:")
print(cosine_values)
print("-" * 30)

# 3. Tangent Operation
# Calculates the tangent of each element.
tangent_values = np.tan(angles_in_radians)
print("Tangent of each element:")
print(tangent_values)
print("-" * 30)

# 4. Inverse Sine (Arcsine)
# Calculates the inverse sine of each element.
# The result is in radians.
inverse_sine = np.arcsin(sine_values)
print("Inverse sine of each element (back to radians):")
print(inverse_sine)
print("-" * 30)

# 5. Converting back to degrees for verification
# Use np.degrees() to convert radians back to degrees.
inverse_sine_degrees = np.degrees(inverse_sine)
print("Inverse sine converted back to degrees:")
print(np.round(inverse_sine_degrees)) # Using np.round to handle small floating-point inaccuracies