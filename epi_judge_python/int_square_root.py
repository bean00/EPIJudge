from test_framework import generic_test

import math


def square_root(k):
    # return use_sqrt_function(k)
    return use_binary_search(k)


# Avg runtime 2 us; Median runtime 3 us
def use_binary_search(k):
    left, right = 0, k

    # Candidate interval [left, right] where everything before left has
    # square <= k, everything after right has square > k
    while left <= right:
        mid = (left + right) // 2
        mid_squared = mid * mid

        if mid_squared <= k:
            left = mid + 1
        else:  # mid_squared > k
            right = mid - 1

    return left - 1


# Avg runtime 1 us; Median runtime 1 us
def use_sqrt_function(k):
    float_square_root = math.sqrt(k)
    int_square_root = math.floor(float_square_root)
    return int_square_root


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_square_root.py",
                                       "int_square_root.tsv", square_root))
