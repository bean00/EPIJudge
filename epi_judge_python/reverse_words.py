import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Assume s is a string encoded as bytearray.
def reverse_words(s):
    for val in s:
        print(val, chr(val))
    # loop through s, creating list of words
    words = []
    word = []
    for val in s:
        if val == 32:
            # if a previous word has been formed
            if len(word) > 0:
                words.append(word)
                word = []
            else:
                words.append([32])
        else:
            word.append(val)

    if len(word) > 0:  # TODO: remove this check?
        words.append(word)

    # reverse words list
    words.reverse()

    # join words with space (32)
    joined = []
    for word in words:
        for val in word:
            joined.append(val)
        joined.append(32)

    del joined[-1]

    joined_as_bytes = bytearray(joined)
    print(joined_as_bytes)
    for i in range(len(s)):
        s[i] = joined_as_bytes[i]
    return s


@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = bytearray()
    s_copy.extend(map(ord, s))

    executor.run(functools.partial(reverse_words, s_copy))

    return s_copy.decode("utf-8")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_words.py", 'reverse_words.tsv',
                                       reverse_words_wrapper))
