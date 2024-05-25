def fibonacci_num_iterative(n):
    num_curr, num_next = 0, 1
    if n == 0:
        return num_curr
    elif n == 1:
        return num_next

    for i in range(2, n + 1):
        temp = num_curr
        num_curr = num_next
        num_next = temp + num_curr

    return num_next


if __name__ == '__main__':
    # 0 1 1 2 3 5 8 13 21 34 55 89
    # 0 1 2 3 4 5 6 7  8  9  10 11
    N = 200
    print(N, fibonacci_num_iterative(N))
