import numpy as np


def fibonacci_num_binet(n):
    phi = (1 + np.sqrt(5)) / 2
    return int((phi ** n - (- phi) ** (- n)) / np.sqrt(5))


if __name__ == '__main__':
    # 0 1 1 2 3 5 8 13 21 34 55 89
    # 0 1 2 3 4 5 6 7  8  9  10 11
    print([fibonacci_num_binet(N) for N in range(15)])
