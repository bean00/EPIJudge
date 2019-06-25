from test_framework import generic_test


def is_palindrome(s):
    clean_str = [c.lower() for c in s if c.isalnum()]
    clean_str = ''.join(clean_str)

    last_idx = len(clean_str) - 1
    mid_idx = last_idx // 2

    for i in range(mid_idx + 1):
        back_idx = last_idx - i
        if clean_str[i] != clean_str[back_idx]:
            return False

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_string_palindromic_punctuation.py",
                                       "is_string_palindromic_punctuation.tsv",
                                       is_palindrome))
