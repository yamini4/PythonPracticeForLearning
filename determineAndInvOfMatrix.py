import numpy as np

# Define a square matrix
A = np.array([[2, 1, 3],
              [1, 0, 2],
              [3, 4, 1]])

# Find the determinant
determinant = np.linalg.det(A)

# Find the inverse (only if determinant ≠ 0)
if determinant != 0:
    inverse = np.linalg.inv(A)
    print("Matrix A:\n", A)
    print("\nDeterminant of A:", determinant)
    print("\nInverse of A:\n", inverse)
else:
    print("Matrix is singular — inverse does not exist.")
