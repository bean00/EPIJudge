from test_framework import generic_test


def is_pattern_contained_in_grid(grid, S):
    return build_up_path(grid, S)


def build_up_path(grid, S):
    path = []
    r = 0
    c = 0
    i = 0
    final_path = build_path(path, S, grid, r, c, i)


def build_path(path, S, grid, r, c, i):
    if len(path) == 0:
        # assume (r, c) is a valid starting point
        # - it's passed in when calling build_path
        return [(r, c)]

    neighbors = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
    valid_neighbors = []
    for r, c in neighbors:
        if (0 <= r < len(grid)) and (0 <= c < len(grid[0])) and (grid[r][c] == S[i]):
            valid_neighbors.append((r, c))

    if len(valid_neighbors) == 0:
        return False

    for r, c in valid_neighbors:
        path.append((r, c))
        return build_path(path, S, grid, r, c, i + 1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_string_in_matrix.py",
                                       'is_string_in_matrix.tsv',
                                       is_pattern_contained_in_grid))
