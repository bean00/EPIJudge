from test_framework import generic_test, test_utils

import copy


def generate_power_set(S):
    return build_power_set(S)


# Avg runtime 8 ms; Median runtime 441 us
def build_power_set(S):
    if not S:
        return [[]]

    sets = build_power_set(S[1:])
    new_sets = []
    for set in sets:
        new_set = copy.deepcopy(set)
        new_set.append(S[0])
        new_sets.append(new_set)

    return sets + new_sets


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("power_set.py", 'power_set.tsv',
                                       generate_power_set,
                                       test_utils.unordered_compare))
