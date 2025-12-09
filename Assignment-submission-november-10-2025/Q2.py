import numpy as np

# Create two matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Matrix multiplication
result = np.dot(A, B)   # or use A @ B
print("Matrix Multiplication Result:\n", result)
