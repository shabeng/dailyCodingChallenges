def bubble_sort_original(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    # print(f'IN: i = {i}, j = {j}')
    return arr


def bubble_sort_early_exit(arr):
    for i in range(len(arr)):
        is_changed = False
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                is_changed = True
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
        if not is_changed:
            # print(f'IN: i = {i}, j = {j}')
            return arr
        else:
            continue
    return arr


def bubble_sort_opt1(arr):
    n = len(arr)
    while n > 1:
        new_n = 0
        for i in range(1, n):
            if arr[i - 1] > arr[i]:
                temp = arr[i - 1]
                arr[i - 1] = arr[i]
                arr[i] = temp
                new_n = i
        n = new_n
    return arr


if __name__ == '__main__':
    import numpy as np
    import time
    exp_num = 50
    res_time_arr = np.zeros(3)

    for j in range(exp_num):
        arr_int = np.random.randint(100000, size=5000)
        for func_ind, func in enumerate([bubble_sort_original, bubble_sort_early_exit, bubble_sort_opt1]):
            ts_algo = time.time()
            arr_sorted = func(arr_int.copy())
            te_algo = time.time()
            res_time_arr[func_ind] += (te_algo - ts_algo)
        if j % 9 == 0:
            print(f'Passed {j + 1} Runs! {exp_num - j - 1} to go...')
    print('Times of Algo:')
    print(res_time_arr / exp_num)
