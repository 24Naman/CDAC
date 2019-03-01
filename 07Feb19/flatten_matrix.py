#!/usr/bin/python3

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
    matrix = np.array(
        [
            [randrange(128) for _ in range(128)] for _ in range(128)
        ]
    )

    print(f"Matrix = \n{matrix}", end="\n\n")

    print(f"Matrix after flattening = {matrix.flatten('F')}")


if __name__ == '__main__':
    main()
