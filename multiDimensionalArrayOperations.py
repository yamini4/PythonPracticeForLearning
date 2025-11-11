import numpy as np

# Define two 2D arrays (matrices)
A = np.array([[2, 4, 6],
              [1, 3, 5]])

B = np.array([[1, 2, 3],
              [4, 5, 6]])

# Perform Arithmetic Operations
sum_arr = A + B           # Addition
diff_arr = A - B          # Subtraction
prod_arr = A * B          # Element-wise Multiplication
div_arr = A / B           # Element-wise Division

# Display Results
print("Array A:\n", A)
print("\nArray B:\n", B)
print("\nAddition (A + B):\n", sum_arr)
print("\nSubtraction (A - B):\n", diff_arr)
print("\nMultiplication (A * B):\n", prod_arr)
print("\nDivision (A / B):\n", div_arr)
