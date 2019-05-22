from test_framework import generic_test

import heapq


def merge_sorted_arrays(sorted_arrays):
    return put_all_elements_in_heap(sorted_arrays)
    # return use_merge_method(sorted_arrays)
    # return keep_k_elements_in_heap(sorted_arrays)


# Avg runtime 111 us; Median runtime 44 us
def put_all_elements_in_heap(sorted_arrays):
    flat_array = [y for x in sorted_arrays for y in x]
    heapq.heapify(flat_array)

    sorted_array = heapq.nsmallest(len(flat_array), flat_array)

    return sorted_array


# Avg runtime 642 us; Median runtime 214 us
# k: number of input sequences
# - Input: [[1, 2, 2], [0, 1], [3, 4]] ==> k = 3
def keep_k_elements_in_heap(sorted_arrays):
    min_heap = []
    # Builds a list of iterators for each array in sorted_arrays
    sorted_arrays_iters = [iter(x) for x in sorted_arrays]

    # Puts first element from each iterator in min_heap
    for i, it in enumerate(sorted_arrays_iters):
        first_element = next(it, None)
        if first_element is not None:
            heapq.heappush(min_heap, (first_element, i))

    result = []
    while min_heap:
        smallest_entry, smallest_array_i = heapq.heappop(min_heap)
        smallest_array_iter = sorted_arrays_iters[smallest_array_i]
        result.append(smallest_entry)
        next_element = next(smallest_array_iter, None)
        if next_element is not None:
            heapq.heappush(min_heap, (next_element, smallest_array_i))

    return result


# Avg runtime 606 us; Median runtime 155 us
def use_merge_method(sorted_arrays):
    return list(heapq.merge(*sorted_arrays))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_arrays_merge.py",
                                       "sorted_arrays_merge.tsv",
                                       merge_sorted_arrays))

    # arrays = [[-1, 0], [-2]]
    # print(merge_sorted_arrays(arrays))
