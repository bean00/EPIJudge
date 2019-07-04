from test_framework import generic_test

from collections import Counter


def can_form_palindrome(s):
    return my_solution(s)
    # return author_solution(s)


# Avg runtime 36 us; Median runtime 6 us
def my_solution(s):
    counts = Counter(s)

    num_odd_counts = 0
    for count in counts.values():
        if count % 2 == 1:
            num_odd_counts += 1
        if num_odd_counts > 1:
            return False

    return True


# Avg runtime 36 us; Median runtime 7 us
def author_solution(s):
    # A string can be permuted to form a palindrome if and only if the number
    # of chars whose frequencies is odd is at most 1
    return sum(v % 2 for v in Counter(s).values()) <= 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "is_string_permutable_to_palindrome.py",
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
