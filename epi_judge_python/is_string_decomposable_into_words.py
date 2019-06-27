import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

import copy


def decompose_into_dictionary_words(domain, dictionary):
    return author_solution(domain, dictionary)


def author_solution(domain, dictionary):
    # When the algorithm finishes, last_length[i] != -1 indicates domain[:i + 1]
    # has a valid decomposition, and the length of the last string in the
    # decomposition is last_length[i]
    last_length = [-1] * len(domain)
    for i in range(len(domain)):
        # If domain[:i + 1] is a dictionary word, set last_length[i] to the
        # length of that word
        if domain[:i + 1] in dictionary:
            last_length[i] = i + 1

        # If last_length[i] = -1 look for j < i such that domain[: j + 1] has a
        # valid decomposition and domain[j + 1:i + 1] is a dictionary word. If
        # so, record the length of that word in last_length[i]
        if last_length[i] == -1:
            for j in range(i):
                if last_length[j] != -1 and domain[j + 1:i + 1] in dictionary:
                    last_length[i] = i - j
                    break

    decompositions = []
    if last_length[-1] != -1:
        # domain can be assembled by dictionary words
        idx = len(domain) - 1
        while idx >= 0:
            decompositions.append(domain[idx + 1 - last_length[idx]:idx + 1])
            idx -= last_length[idx]
        decompositions = decompositions[::-1]

    return decompositions


def my_solution(domain, dictionary):
    words = []
    final_words_list = build_list_of_words(domain, dictionary, domain, words)
    print(final_words_list)

    return final_words_list


def build_list_of_words(domain, dictionary, curr_domain, words):
    if not curr_domain:
        return words

    starting_words = get_starting_words(curr_domain, dictionary)
    if not starting_words:
        return words

    all_words_lists = []

    for starting_word in starting_words:
        words_copy = copy.deepcopy(words)
        words_copy.append(starting_word)
        offset = len(starting_word)

        words_list = build_list_of_words(domain, dictionary, curr_domain[offset:], words_copy)
        all_words_lists.append(words_list)

    final_words_list = []
    for words_list in all_words_lists:
        if words_list and len(domain) == len(''.join(words_list)):
            final_words_list = words_list

    return final_words_list


# Time: O(n), n - # of characters in domain
def get_starting_words(domain, dictionary):
    words = []

    for i in range(len(domain)):
        starting_word = domain[0:i + 1]
        if starting_word in dictionary:
            words.append(starting_word)

    return words


@enable_executor_hook
def decompose_into_dictionary_words_wrapper(executor, domain, dictionary,
                                            decomposable):
    result = executor.run(
        functools.partial(decompose_into_dictionary_words, domain, dictionary))

    if not decomposable:
        if result:
            raise TestFailure('domain is not decomposable')
        return

    if any(s not in dictionary for s in result):
        raise TestFailure('Result uses words not in dictionary')

    if ''.join(result) != domain:
        raise TestFailure('Result is not composed into domain')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "is_string_decomposable_into_words.py",
            'is_string_decomposable_into_words.tsv',
            decompose_into_dictionary_words_wrapper))
