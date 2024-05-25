import numpy as np
from functools import reduce


def find_missing_num_sum_comparison(arr):
    """
    Compares between the expected sum given the known formula of series sum
    :param arr: list of int, the array with one missing element between 1, n + 1
    :return: int, the missing element
    """
    n = len(arr)
    sum_arr_expected = (n + 1) * (1 + n + 1) / 2
    sum_arr_missing = sum(arr)
    return sum_arr_expected - sum_arr_missing


def find_missing_num_xor_operation(arr):
    """
    Compraes between the XOR value of the full array to the one of the missing one.
    The difference is the missing value.
    :param arr: list of int, the array with one missing element between 1, n + 1
    :return: int, the missing element
    """
    xor_full = reduce(lambda x, y: x ^ y, np.arange(len(arr) + 1) + 1)
    xor_missing = reduce(lambda x, y: x ^ y, arr)
    return np.abs(xor_missing - xor_full)


if __name__ == '__main__':
    N = 4
    ind_miss = np.random.randint(N)
    arr_full = list(np.arange(N) + 1)
    miss_num = arr_full.pop(ind_miss)
    miss_num_alg_sum = find_missing_num_sum_comparison(arr_full)
    miss_num_alg_xor = find_missing_num_xor_operation(arr_full)
    assert miss_num_alg_sum == miss_num, f'WRONG! {miss_num}, {miss_num_alg_sum}'
    assert miss_num_alg_xor == miss_num, f'WRONG! {miss_num}, {miss_num_alg_xor}'
