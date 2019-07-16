from test_framework import generic_test

from collections import deque


# Avg runtime 12 us; Median runtime 2 us
def is_well_formed(s):
    d = deque()
    char_map = {'{': '}', '(': ')', '[': ']'}

    for char in s:
        if char in char_map:
            d.append(char)
        elif not d or char_map[d.pop()] != char:
            return False

    is_d_empty = not d
    return is_d_empty


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_valid_parenthesization.py",
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
