import numpy as np

# Coefficient matrix
A = np.array([[2, 1],
              [1, -1]])

# Constant matrix
B = np.array([5, 1])

# Solve the system of equations
solution = np.linalg.solve(A, B)

# Display result
x, y = solution
print(f"x = {x}")
print(f"y = {y}")
