from test_framework import generic_test


# Avg runtime 26 us; Median runtime 27 us
def is_valid_sudoku(partial_assignment):
    rows = [[] for _ in range(9)]
    cols = [[] for _ in range(9)]
    sub_arrays = [[] for _ in range(9)]

    for i in range(9):
        for j in range(9):
            val = partial_assignment[i][j]
            if val != 0:
                rows[i].append(val)
                cols[j].append(val)

                # add to appropriate list in sub_arrays
                row_idx, col_idx = i // 3, j // 3
                k = col_idx + (3 * row_idx)  # calc 0-8 from row (0-2) and col (0-2)
                sub_arrays[k].append(val)

    for li in rows + cols + sub_arrays:
        li_as_set = set(li)
        if len(li) != len(li_as_set):
            return False

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_valid_sudoku.py",
                                       "is_valid_sudoku.tsv", is_valid_sudoku))
