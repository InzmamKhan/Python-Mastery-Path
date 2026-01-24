import numpy as np

# --- Array of Zeroes ---
a = np.zeros((2,3))
print(f"Array of Zeroes : {a} \n")

# --- Array of Ones ---
b = np.ones((2,3))
print(f"Array of Ones : {b} \n")


# --- Array of 10's ---
c = np.full((2,3), 10)
print(f"Array of 10's : {c} \n ")

# --- Array of Random Numbers ---
d = np.random.random((2,3))
print(f"Array of Random Numbers : {d} \n")

# --- Identity Matrix ---
e = np.identity(5)
print(f"Identity Matrix : {e} \n")