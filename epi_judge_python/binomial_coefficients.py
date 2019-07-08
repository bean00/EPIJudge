from test_framework import generic_test


def compute_binomial_coefficient(n, k):
    # return my_solution(n, k)
    return author_solution(n, k)


# Avg runtime 17 ms; Median runtime 442 us
def my_solution(n, k):
    result = [[1] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, k + 1):
            result[i][j] = result[i][j - 1] + result[i - 1][j]

    return result[n - k][k]


# Avg runtime 1 ms; Median runtime 435 us
def author_solution(n, k):
    def compute_x_choose_y(x, y):
        if y in (0, x):
            return 1

        if x_choose_y[x][y] == 0:
            without_y = compute_x_choose_y(x - 1, y)
            with_y = compute_x_choose_y(x - 1, y - 1)
            x_choose_y[x][y] = without_y + with_y
        return x_choose_y[x][y]

    x_choose_y = [[0] * (k + 1) for _ in range(n + 1)]
    return compute_x_choose_y(n, k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("binomial_coefficients.py",
                                       'binomial_coefficients.tsv',
                                       compute_binomial_coefficient))
