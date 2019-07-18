from test_framework import generic_test


def number_of_ways_to_top(top, maximum_step):
    # return my_solution(top, maximum_step)
    return author_solution(top, maximum_step)


# Avg runtime 23 us; Median runtime 19 us
def my_solution(top, maximum_step):
    num_ways = [0] * (top + 1)
    num_ways[0] = num_ways[1] = 1

    for i in range(2, top + 1):
        curr_num_ways = 0
        for j in range(1, maximum_step + 1):
            curr_num_ways += num_ways[i - j]
        num_ways[i] = curr_num_ways

    return num_ways[-1]


# Avg runtime 53 us; Median runtime 48 us
def author_solution(top, maximum_step):
    def compute_number_of_ways_to_h(h):
        if h <= 1:
            return 1

        if number_of_ways_to_h[h] == 0:
            number_of_ways_to_h[h] = sum(
                compute_number_of_ways_to_h(h - i)
                for i in range(1,
                               min(maximum_step, h) + 1))
        return number_of_ways_to_h[h]

    number_of_ways_to_h = [0] * (top + 1)
    return compute_number_of_ways_to_h(top)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_traversals_staircase.py",
                                       "number_of_traversals_staircase.tsv",
                                       number_of_ways_to_top))
