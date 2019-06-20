from test_framework import generic_test

from collections import defaultdict


def find_nearest_repetition(paragraph):
    min_dist = float('inf')
    indices = defaultdict(int)

    for i, word in enumerate(paragraph):
        if word in indices:
            last_i = indices[word]
            dist = i - last_i
            min_dist = min(dist, min_dist)
        indices[word] = i

    final_min_dist = min_dist if min_dist != float('inf') else -1
    return final_min_dist


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("nearest_repeated_entries.py",
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
