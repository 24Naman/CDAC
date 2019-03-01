#!/usr/bin/python

"""
    2/21/19: Naman

    to generate input data with intercept and slope, with variance

"""

import numpy as np
import random


def prepare_input_data(_intercept, _slope, _variance, _no_of_inputs):
    x = np.zeros(shape=(_no_of_inputs, 2))  # x is m by 2.
    y = np.zeros(shape=(_no_of_inputs, 1))

    for index in range(_no_of_inputs):
        x[index][0] = 1  # 0th column represents 1 for bias terms for each row
        x[index][1] = index  # 1st column represents index for sample for each row
        y[index] = (_intercept + index * _slope) + random.uniform(0, 1) * _variance

    return x, y


def gradient_descent(_x, _y, _theta, _alpha, _no_of_inputs):
    hypothesis = _x.dot(_theta)
    error = hypothesis - _y
    cost = 1 / (2 * _no_of_inputs) * np.sum(error ** 2)
    gradient = 1 / _no_of_inputs * _x.T.dot(error)
    _theta = _theta - _alpha * gradient
    return _theta, cost


if __name__ == "__main__":
    # preparing training data
    """ By updating following members this program can be worked for 
        different sizes of data sets with different aplha, iteration counts"""
    intercept = 20
    slope = 32
    variance = 2
    no_of_inputs = 2
    alpha = 0.1
    no_of_iterations = 200
    cost = 0

    # generates data set which fits close to y=intercept+slope*x
    x, y = prepare_input_data(intercept, slope, variance, no_of_inputs)
    theta = np.ones(shape=(2, 1))

    # fit model
    for i in range(no_of_iterations):
        theta, cost = gradient_descent(x, y, theta, alpha, no_of_inputs)
        if i % 10 == 0:
            print("theta", theta)
            print("cost", cost)
            print("iteration", i)
            input("enter some input")
        if cost < 1e-6:
            print(" theta has been found")
            break

    print("theta", theta)
    print("cost", cost)
