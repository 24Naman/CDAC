#!/usr/bin/python

"""
    1/30/19: Naman
"""

import numpy as np


def main():
    """
        Main Function
    """
    first = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
    second = np.array([
        [1],
        [2],
        [3]
    ])

    print("Array Broadcasting ->", first + second, sep='\n')
    print("Array Hadamand Product ->", first * second, sep='\n')
    print("Array Dot Product ->", np.dot(first, second), sep='\n')
    matrix = np.array([
        [0, 3, -2],
        [1, -4, -2],
        [-3, 4, 1]
    ])
    print("Determinant of the array ->", np.linalg.det(matrix))
    print("Inverse of the array ->", np.linalg.inv(matrix), sep='\n')
    print("A . A` ->", np.dot(matrix, np.linalg.inv(matrix)), sep='\n')
    print("------------")


if __name__ == "__main__":
    main()
