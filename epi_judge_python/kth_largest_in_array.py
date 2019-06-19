from test_framework import generic_test

import heapq
import operator
import random


def find_kth_largest(k, A):
    # return use_min_heap(k, A)
    return use_pivot_and_partition(k, A)


# Avg runtime 21 us; Median runtime 4 us
def use_min_heap(k, A):
    min_heap = A[:k]
    heapq.heapify(min_heap)

    for elem in A[k:]:
        heapq.heappushpop(min_heap, elem)

    kth_largest = min_heap[0]
    return kth_largest


# Avg runtime 123 us; Median runtime 20 us
def use_pivot_and_partition(k, A):
    def find_kth(comp):
        # Partition A[left:right + 1] around pivot_idx, returns the new index of
        # the pivot, new_pivot_idx, after partition. After partitioning,
        # A[left:new_pivot_idx] contains elements that are "greater than" the
        # pivot, and A[new_pivot_idx + 1: right + 1] contains elements that are
        # "less than" the pivot.
        def partition_around_pivot(left, right, pivot_idx):
            pivot_value = A[pivot_idx]
            new_pivot_idx = left
            A[pivot_idx], A[right] = A[right], A[pivot_idx]
            for i in range(left, right):
                # if A[i] > pivot_value:
                if comp(A[i], pivot_value):
                    A[i], A[new_pivot_idx] = A[new_pivot_idx], A[i]
                    new_pivot_idx += 1
            A[right], A[new_pivot_idx] = A[new_pivot_idx], A[right]
            return new_pivot_idx

        left, right = 0, len(A) - 1
        while left <= right:
            pivot_idx = random.randint(left, right)
            new_pivot_idx = partition_around_pivot(left, right, pivot_idx)
            if new_pivot_idx == k - 1:
                return A[new_pivot_idx]
            elif new_pivot_idx > k - 1:
                right = new_pivot_idx - 1
            else:  # new_pivot_idx < k - 1
                left = new_pivot_idx + 1

    return find_kth(operator.gt)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("kth_largest_in_array.py",
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
