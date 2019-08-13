from test_framework import generic_test


def matrix_search(A, x):
    return my_solution(A, x)


def my_solution(A, x):
    num_rows, num_cols = len(A), len(A[0])
    r, c = 0, num_cols - 1

    while r <= num_rows - 1 and c >= 0:
        if A[r][c] == x:
            return True
        elif A[r][c] < x:
            r += 1
        else:  # A[r][c] > x
            c -= 1

    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_row_col_sorted_matrix.py",
                                       'search_row_col_sorted_matrix.tsv',
                                       matrix_search))
