#!/usr/bin/python

"""
    2/20/19: Naman

    J = w1^2 + w2^2 + 4w1 - 6w2 - 7

    To find J
"""

ALPHA = 1
W0, W1 = 0, 0
X = [0, 0.25, 0.50, 0.75, 1.00]
Y = [0.8822, 1.2165, 1.3171, 1.7930, 1.9826]
X = [1, 2, 4, 0]
Y = [0.5, 1, 2, 0]
ALPHA = 0.1
W0, W1 = 1, 1
M = len(X)


def return_j(w0, w1):
    """
    return value of J
    :param w0:
    :param w1:
    :return:
    """
    return sum((y - (w1 * x) - w0) ** 2 for x, y in zip(X, Y)) / M


def main():
    """
        Main Function
    """
    global W0, W1

    for i in range(1000):
        print(f"i = {i} -> j = {return_j(w0=W0, w1=W1)} \t W0 = {W0} \t W1 = {W1}")

        def y_i_cap(x):
            return (W1 * x) + W0

        temp_w0 = W0 - ALPHA * (sum([y - y_i_cap(x) for x, y in zip(X, Y)]) / -M)
        temp_w1 = W1 - ALPHA * (sum([(y - y_i_cap(x)) * x for x, y in zip(X, Y)]) / -M)

        W0, W1 = temp_w0, temp_w1


if __name__ == "__main__":
    main()
