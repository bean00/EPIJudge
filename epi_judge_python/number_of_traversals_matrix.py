from test_framework import generic_test


def number_of_ways(r, c):
    return iteratively(r, c)
    # return recursively(r, c)


# My solution
# Avg runtime 32 us; Median runtime 29 us
def iteratively(r, c):
    arr = [[1] * c] * r

    for i in range(1, r):
        for j in range(1, c):
            arr[i][j] = arr[i][j - 1] + arr[i - 1][j]

    return arr[r - 1][c - 1]


# EPI solution
# Avg runtime 100 us; Median runtime 88 us
def recursively(n, m):
    def compute_number_of_ways_to_xy(x, y):
        if x == y == 0:
            return 1

        if recursively[x][y] == 0:
            ways_top = 0 if x == 0 else compute_number_of_ways_to_xy(x - 1, y)
            ways_left = 0 if y == 0 else compute_number_of_ways_to_xy(x, y - 1)
            recursively[x][y] = ways_top + ways_left
        return recursively[x][y]

    recursively = [[0] * m for _ in range(n)]
    return compute_number_of_ways_to_xy(n - 1, m - 1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_traversals_matrix.py",
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))

    # print(number_of_ways(3, 4))
