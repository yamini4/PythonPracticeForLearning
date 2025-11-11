import numpy as np

# Define an array
arr = np.array([4, 9, 16, 25, 36])

# Apply square root function
sqrt_arr = np.sqrt(arr)

print("Original Array:", arr)
print("Square Root of Each Element - float:", sqrt_arr)
print("Square Root of Each Element - int:", sqrt_arr.astype(int))
print("Data type of elements in sqrt_arr:", sqrt_arr.dtype)

print("===================================================================================")

def square_root(x):
    return x ** 0.5

arr = np.array([1, 4, 9, 16])
result = np.array(list(map(square_root, arr)), dtype=int)   # 👈 convert to int
print("Integer Results:", result)
print("Data type of elements:", result.dtype)
