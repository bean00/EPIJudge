from test_framework import generic_test


def intersect_two_sorted_arrays(A, B):
    i, j, arr = 0, 0, []

    while i < len(A) and j < len(B):
        if arr and A[i] == arr[-1]:
            i += 1
        elif A[i] < B[j]:
            i += 1
        elif A[i] == B[j]:
            arr.append(A[i])
            i, j = i + 1, j + 1
        else:  # A[i] > B[j]
            j += 1

    return arr


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("intersect_sorted_arrays.py",
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
