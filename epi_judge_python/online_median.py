from test_framework import generic_test

import heapq


def online_median(sequence):
    min_heap = []
    max_heap = []
    result = []

    for elem in sequence:
        for_max = -heapq.heappushpop(min_heap, elem)
        heapq.heappush(max_heap, for_max)

        if len(max_heap) > len(min_heap):
            for_min = -heapq.heappop(max_heap)
            heapq.heappush(min_heap, for_min)

        if len(min_heap) > len(max_heap):
            curr_median = min_heap[0]
        else:
            curr_median = (min_heap[0] + -max_heap[0]) / 2

        result.append(curr_median)

    return result


def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("online_median.py", "online_median.tsv",
                                       online_median_wrapper))
