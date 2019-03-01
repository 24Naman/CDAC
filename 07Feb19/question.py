#!/usr/bin/python3

"""
    Eigenvalues, eigen vectors
"""

import numpy as np


INPUT_MATRIX = np.array([
    [1, 3, 2, 4, 6],
    [3, 2, 7, 8, 7],
    [2, 7, 3, 7, 8],
    [4, 8, 7, 4, 9],
    [6, 7, 8, 9, 5]
])

print("Eigenvalues = \n", np.linalg.eigvals(INPUT_MATRIX))
print("Eigen vectors = \n", np.linalg.eig(INPUT_MATRIX))

print(f"Square Root of Maximum Eigenvalue of A^2 \
= {np.sqrt(max(np.linalg.eigvals(np.matmul(INPUT_MATRIX, INPUT_MATRIX))))}")
