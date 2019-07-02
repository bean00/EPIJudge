from test_framework import generic_test

import heapq


def sort_approximately_sorted_array(sequence, k):
    min_heap, sorted = [], []

    for _ in range(k):
        heapq.heappush(min_heap, next(sequence))

    for elem in sequence:
        smallest = heapq.heappushpop(min_heap, elem)
        sorted.append(smallest)

    rest_of_heap_sorted = heapq.nsmallest(k, min_heap)
    sorted += rest_of_heap_sorted

    return sorted


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "sort_almost_sorted_array.py", 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
