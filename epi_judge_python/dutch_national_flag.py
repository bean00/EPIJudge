import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def dutch_flag_partition(pivot_i, A):
    partition_one_pass(pivot_i, A)


# Avg running time: 54 us; Median running time: 8 us
def partition_two_passes(pivot_i, A):
    pivot = A[pivot_i]
    # First pass: group elements smaller than pivot
    smaller = 0
    for i in range(len(A)):
        if A[i] < pivot:
            A[i], A[smaller] = A[smaller], A[i]
            smaller += 1
    # Second pass: group elements larger than pivot
    larger = len(A) - 1
    for i in reversed(range(len(A))):
        if A[i] > pivot:
            A[i], A[larger] = A[larger], A[i]
            larger -= 1


# Avg running time: 52 us; Median running time: 8 us
def partition_one_pass(pivot_i, A):
    pivot = A[pivot_i]
    # Keep the following invariants during partitioning:
    # bottom group: A[:smaller]
    # middle group: A[smaller:equal]
    # unclassified group: A[equal:larger]
    # top group: A[larger:]
    smaller, equal, larger = 0, 0, len(A)
    while equal < larger:
        # A[equal] is the incoming unclassified element
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller, equal = smaller + 1, equal + 1
        elif A[equal] == pivot:
            equal += 1
        else:  # A[equal] > pivot
            larger -= 1
            A[larger], A[equal] = A[equal], A[larger]


def partition_my_solution(pivot_i, A):
    next_less, next_equal, next_greater = 0, pivot_i + 1, len(A) - 1
    equal_offset = 1
    pivot = A[pivot_i]

    if next_equal >= next_greater:
        next_equal = pivot_i - 1
        equal_offset = -1

    for i in range(len(A)):
        while True:
            if i < pivot_i:
                if (A[i] < pivot) or (next_equal < i):
                    break
                elif A[i] == pivot:
                    if next_equal >= next_greater:
                        next_equal = pivot_i - 1
                        equal_offset = -1

                    temp = A[next_equal]
                    A[next_equal] = A[i]
                    A[i] = temp
                    next_equal += equal_offset
                else:
                    temp = A[next_greater]
                    A[next_greater] = A[i]
                    A[i] = temp
                    next_greater -= 1
            elif pivot_i <= i < next_equal:
                break
            elif next_equal < i <= next_greater:
                break
            else:
                if (A[i] > pivot) and (i >= next_greater):
                    break
                elif (A[i] == pivot) and (i <= next_equal):
                    break
                elif A[i] == pivot:
                    if next_equal >= next_greater:
                        next_equal = pivot_i - 1
                        equal_offset = -1

                    temp = A[next_equal]
                    A[next_equal] = A[i]
                    A[i] = temp
                    next_equal += equal_offset
                elif A[i] > pivot:
                    temp = A[next_greater]
                    A[next_greater] = A[i]
                    A[i] = temp
                    next_greater -= 1
                else:
                    temp = A[next_less]
                    A[next_less] = A[i]
                    A[i] = temp
                    next_less += 1


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure("Some elements are missing from original array")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("dutch_national_flag.py",
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))

    # pivot_i = 8
    # A = [0, 2, 1, 1, 0, 0, 2, 0, 1, 0, 2, 2, 0, 1, 2, 0, 2]
    # pivot_i = 2
    # A = [0, 1, 1, 2]
    # pivot_i = 0
    # A = [0, 1, 0, 2, 0, 1, 1, 0, 0, 2, 2, 1, 2, 1, 0, 0, 2, 2, 1, 2, 2, 1, 1, 0, 2, 2, 0, 2, 0, 2, 0, 2, 0, 2, 1, 0, 2, 1, 1, 2, 2, 1, 1, 0, 2, 1, 2, 2, 0, 2, 2, 2, 1, 1, 1, 0, 2, 0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 0, 1, 2, 2, 1, 1, 0, 2, 0, 1, 1, 2, 0, 0, 2, 1, 0, 2, 1, 0, 2, 1, 2, 2, 0, 2, 1, 2, 2, 1]
    # A = [0, 1, 0, 2]

    # dutch_flag_partition(pivot_i, A)
    # print(A)
