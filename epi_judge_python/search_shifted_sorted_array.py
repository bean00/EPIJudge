from test_framework import generic_test


def search_smallest(A):
    # return my_solution(A)
    return author_solution(A)


def author_solution(A):
    left, right = 0, len(A) - 1

    # right will save index of smallest element
    while left < right:
        mid = (left + right) // 2
        if A[mid] > A[right]:
            left = mid + 1
        else:  # A[mid] < A[right]
            right = mid

    # after loop, left == right, so can return either for smallest index
    return left


def my_solution(A):
    left = 0
    right = smallest_i = len(A) - 1

    while left <= right:
        mid_i = (left + right) // 2
        if A[mid_i] < A[smallest_i]:
            smallest_i = mid_i
            right = mid_i - 1
        else:  # A[mid_i] > A[smallest_i]
            left = mid_i + 1

    return smallest_i


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_shifted_sorted_array.py",
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
