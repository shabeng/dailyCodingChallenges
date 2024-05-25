def fibonacci_num_memoization(n):
    memo_dict = {0: 0, 1: 1}

    def fibonacci_num_memoization_helper(n_):
        if n_ not in memo_dict:
            fn1 = fibonacci_num_memoization_helper(n_ - 1)
            fn2 = fibonacci_num_memoization_helper(n_ - 2)
            memo_dict[n_ - 1] = fn1
            memo_dict[n_ - 2] = fn2
            memo_dict[n_] = fn1 + fn2
        return memo_dict[n_]

    fibonacci_num_memoization_helper(n)
    return memo_dict[n]


if __name__ == '__main__':
    # 0 1 1 2 3 5 8 13 21 34 55 89
    # 0 1 2 3 4 5 6 7  8  9  10 11
    print([fibonacci_num_memoization(N) for N in range(15)])
