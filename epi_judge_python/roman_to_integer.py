from test_framework import generic_test

import functools


values = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50,
    'C': 100, 'D': 500, 'M': 1000
}

exceptions = {
    'I': {'V', 'X'},
    'X': {'L', 'C'},
    'C': {'D', 'M'}
}


def roman_to_integer(s):
    return my_solution(s)
    # return author_solution(s)


# Avg runtime 3 us; Median runtime 4 us
def my_solution(s):
    result = i = 0

    while i < len(s):
        at_least_two_chars_left = (i <= len(s) - 2)
        # *Note: can just check that value of current char < value of next char
        # Ex: XL, X (10) < L (50)
        # if at_least_two_chars_left and values[s[i]] < values[s[i + 1]]:
        if at_least_two_chars_left and is_exception(s[i], s[i + 1]):
            result -= values[s[i]]
            result += values[s[i + 1]]
            i += 2
        else:
            result += values[s[i]]
            i += 1

    return result


def is_exception(c1, c2):
    return (c1 in exceptions) and (c2 in exceptions[c1])


# Avg runtime 3 us; Median runtime 4 us
def author_solution(s):
    return functools.reduce(
        lambda val, i: val + (-values[s[i]] if values[s[i]] < values[s[i + 1]] else values[s[i]]),
        reversed(range(len(s) - 1)), values[s[-1]])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "roman_to_integer.py", 'roman_to_integer.tsv', roman_to_integer))
