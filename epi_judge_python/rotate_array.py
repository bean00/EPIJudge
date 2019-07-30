import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Avg runtime 76 us; Median runtime 7 us
def rotate_array(rotate_amount, A):
    start, end = 0, len(A) - 1
    rotate_amount %= len(A)
    last_elem_i = rotate_amount - 1

    reverse_in_place(A, start, end)

    reverse_in_place(A, start, last_elem_i)
    reverse_in_place(A, last_elem_i + 1, end)


def reverse_in_place(A, start, end):
    mid = (start + end) // 2

    for i in range(start, mid + 1):
        j = end - (i - start)
        A[i], A[j] = A[j], A[i]


@enable_executor_hook
def rotate_array_wrapper(executor, A, rotate_amount):
    a_copy = A[:]
    executor.run(functools.partial(rotate_array, rotate_amount, a_copy))
    return a_copy


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("rotate_array.py", 'rotate_array.tsv',
                                       rotate_array_wrapper))
