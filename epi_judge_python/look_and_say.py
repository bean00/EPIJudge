from test_framework import generic_test

import itertools


def look_and_say(n):
    # return my_solution(n)
    # return author_solution(n)
    return author_solution_pythonic(n)


# Avg runtime 2 ms; Median runtime 189 us
def my_solution(n):
    digits = [1]

    for _ in range(n - 1):
        next_digits = []
        curr_digit, curr_count = digits[0], 0

        for digit in digits:
            if digit != curr_digit:
                next_digits += [curr_count, curr_digit]
                curr_digit, curr_count = digit, 1
            else:
                curr_count += 1

        next_digits += [curr_count, curr_digit]
        digits = next_digits

    digits_str = ''.join([str(x) for x in digits])
    return digits_str


# Avg runtime 9 ms; Median runtime 566 us
def author_solution(n):
    def next_number(s):
        result, i = [], 0
        while i < len(s):
            count = 1
            while i + 1 < len(s) and s[i] == s[i + 1]:
                i += 1
                count += 1
            result.append(str(count) + s[i])
            i += 1
        return ''.join(result)

    s = '1'
    for _ in range(1, n):
        s = next_number(s)
    return s


# Avg runtime 7 ms; Median runtime 473 us
def author_solution_pythonic(n):
    s = '1'
    for _ in range(n - 1):
        s = ''.join(
            str(len(list(group))) + key for key, group in itertools.groupby(s))
    return s


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("look_and_say.py", "look_and_say.tsv",
                                       look_and_say))
