import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size, s):
    return do_in_place(size, s)


# Avg runtime 20 us; Median runtime 4 us
def do_in_place(size, s):
    j = len(s) - 1

    for i in reversed(range(size)):
        if s[i] == 'b':
            continue
        elif s[i] == 'a':
            s[j - 1:j + 1] = 'd', 'd'
            j -= 2
        else:  # s[i] is not 'a' or 'b'
            s[j] = s[i]
            j -= 1

    del s[:j + 1]

    return s


def convert_then_replace(size, s):
    s = ''.join(s)
    s = s[:size]
    s = s.replace('b', '')
    s = s.replace('a', 'dd')
    s = list(s)

    return s


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:len(res_size)]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("replace_and_remove.py",
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
