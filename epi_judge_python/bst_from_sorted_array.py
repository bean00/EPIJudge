import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import (binary_tree_height,
                                              generate_inorder)
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

from bst_node import BstNode


def build_min_height_bst_from_sorted_array(A):
    return build_tree(A)
    # return author_solution(A)


# Avg runtime 44 us; Median runtime 14 us
def build_tree(A):
    if not A:
        return None

    mid_i = (len(A)- 1) // 2
    mid_elem = A[mid_i]

    node = BstNode(mid_elem)
    node.left = build_tree(A[:mid_i])
    node.right = build_tree(A[mid_i + 1:])

    return node


# Avg runtime 33 us; Median runtime 10 us
def author_solution(A):
    def build_min_height_bst_from_sorted_subarray(start, end):
        if start >= end:
            return None
        mid = (start + end) // 2
        return BstNode(A[mid],
                       build_min_height_bst_from_sorted_subarray(start, mid),
                       build_min_height_bst_from_sorted_subarray(mid + 1, end))

    return build_min_height_bst_from_sorted_subarray(0, len(A))


@enable_executor_hook
def build_min_height_bst_from_sorted_array_wrapper(executor, A):
    result = executor.run(
        functools.partial(build_min_height_bst_from_sorted_array, A))

    if generate_inorder(result) != A:
        raise TestFailure("Result binary tree mismatches input array")
    return binary_tree_height(result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "bst_from_sorted_array.py", 'bst_from_sorted_array.tsv',
            build_min_height_bst_from_sorted_array_wrapper))
