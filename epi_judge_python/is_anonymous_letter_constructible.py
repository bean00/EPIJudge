from test_framework import generic_test

from collections import Counter


def is_letter_constructible_from_magazine(letter_text, magazine_text):
    # return count_chars(letter_text, magazine_text)
    return delete_finished_chars(letter_text, magazine_text)


# My solution
# Avg runtime 326 us; Median runtime 24 us (using Counter())
def count_chars(letter, magazine):
    counts = Counter(letter)

    for c in magazine:
        counts[c] -= 1

    for val in counts.values():
        if val > 0:
            return False

    return True


# EPI solution
# Avg runtime 126 us; Median runtime 23 us
def delete_finished_chars(letter, magazine):
    counts = Counter(letter)

    for c in magazine:
        if c in counts:
            counts[c] -= 1

            if counts[c] == 0:
                del counts[c]

                if not counts:
                    return True

    return not counts


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_anonymous_letter_constructible.py",
                                       'is_anonymous_letter_constructible.tsv',
                                       is_letter_constructible_from_magazine))

    # letter_text = 'GATTACA'
    # magazine_text = 'A AD FS GA T ACA TTT'
    # print(is_letter_constructible_from_magazine(letter_text, magazine_text))
