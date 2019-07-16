from test_framework import generic_test


def maximum_revenue(coins):
    return author_solution(coins)


# Avg runtime 5 ms; Median runtime 157 us
def author_solution(coins):
    def compute_maximum_revenue_for_range(a, b):
        if a > b:
            # No coins left
            return 0

        if maximum_revenue_for_range[a][b] == 0:
            max_revenue_a = coins[a] + min(
                compute_maximum_revenue_for_range(a + 2, b),
                compute_maximum_revenue_for_range(a + 1, b - 1))
            max_revenue_b = coins[b] + min(
                compute_maximum_revenue_for_range(a + 1, b - 1),
                compute_maximum_revenue_for_range(a, b - 2))
            maximum_revenue_for_range[a][b] = max(max_revenue_a, max_revenue_b)
        return maximum_revenue_for_range[a][b]

    maximum_revenue_for_range = [[0] * len(coins) for _ in coins]
    return compute_maximum_revenue_for_range(0, len(coins) - 1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "picking_up_coins.py", 'picking_up_coins.tsv', maximum_revenue))
