from test_framework import generic_test


def minimum_path_weight(triangle):
    return my_solution(triangle)
    # return author_solution(triangle)


# Avg runtime 436 us; Median runtime 360 us
def my_solution(triangle):
    if not triangle:
        return 0
    num_rows = len(triangle)
    path_weights = triangle[num_rows - 1][:]

    for i in reversed(range(len(triangle) - 1)):
        for j in range(i + 1):
            cell_weight = triangle[i][j]
            bottom_left_weight = path_weights[j]
            bottom_right_weight = path_weights[j + 1]
            path_weights[j] = min(bottom_left_weight, bottom_right_weight) + cell_weight

    min_path_weight = path_weights[0]
    return min_path_weight


# Avg runtime 961 us; Median runtime 811 us
def author_solution(triangle):
    min_weight_to_curr_row = [0]
    for row in triangle:
        min_weight_to_curr_row = [
            row[j] +
            min(min_weight_to_curr_row[max(j - 1, 0)],
                min_weight_to_curr_row[min(j,
                                           len(min_weight_to_curr_row) - 1)])
            for j in range(len(row))
        ]
    return min(min_weight_to_curr_row)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("minimum_weight_path_in_a_triangle.py",
                                       'minimum_weight_path_in_a_triangle.tsv',
                                       minimum_path_weight))
