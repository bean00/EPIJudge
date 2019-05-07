from test_framework import generic_test
from test_framework.test_failure import TestFailure

INT_TO_CHAR_OFFSET = 48


def int_to_string(x):
    digits = []
    sign = ''

    if x < 0:
        sign = '-'
        x *= -1
    elif x == 0:
        return '0'

    while x > 0:
        right_digit = x % 10
        right_str = chr(right_digit + INT_TO_CHAR_OFFSET)
        digits.append(right_str)
        x //= 10

    digits.append(sign)
    digits.reverse()
    final_str = ''.join(digits)

    return final_str


def string_to_int(s):
    digits = []
    sum = 0
    multiplier = 1
    sign = 1

    if s[0] == '-':
        sign = -1
        s = s[1:]

    for c in reversed(s):
        digit = ord(c) - INT_TO_CHAR_OFFSET
        digits.append(digit)

    for digit in digits:
        sum += digit * multiplier
        multiplier *= 10

    return sum * sign


def wrapper(x, s):
    if int_to_string(x) != s:
        raise TestFailure("Int to string conversion failed")
    if string_to_int(s) != x:
        raise TestFailure("String to int conversion failed")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("string_integer_interconversion.py",
                                       'string_integer_interconversion.tsv',
                                       wrapper))
