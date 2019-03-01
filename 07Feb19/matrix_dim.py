#!/usr/bin/python

"""
    07-02-2019
    Author: Naman Jain

"""

from random import randrange
import numpy as np


def main():
    """
        Main Function
    """
    matrix_one = np.array([[randrange(2) for i in range(2)] for _ in range(2)])
    print(f"Matrix One = \n{matrix_one}")

    matrix_two = np.array([[randrange(16) for i in range(16)] for _ in range(16)])
    print(f"Matrix One = \n{matrix_two}")

    product_matrix = np.matmul(matrix_one, matrix_two)
    print(f"Product Matrix = \n{product_matrix}")

    answer_matrix = np.matmul(product_matrix, np.linalg.inv(matrix_one))
    print(f"Answer Matrix = \n{answer_matrix}")


if __name__ == '__main__':
    main()
