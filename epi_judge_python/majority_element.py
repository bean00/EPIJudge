from test_framework import generic_test


def majority_search(stream):
    curr_elem, count = None, 0

    for elem in stream:
        if count == 0:
            curr_elem = elem
            count = 1
        elif elem == curr_elem:
            count += 1
        else:  # elem != curr_elem
            count -= 1

    return curr_elem


def majority_search_wrapper(stream):
    return majority_search(iter(stream))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("majority_element.py",
                                       'majority_element.tsv',
                                       majority_search_wrapper))
