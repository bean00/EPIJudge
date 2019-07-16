from test_framework import generic_test


# Avg runtime 26 us; Median runtime 6 us
def even_odd_merge(L):
    if not L or not L.next:
        return L

    curr_ptr = L
    next_ptr = odd_head = L.next
    num_changes = 0

    while next_ptr.next:
        curr_ptr.next = next_ptr.next
        curr_ptr = next_ptr
        next_ptr = next_ptr.next
        num_changes += 1

    if num_changes % 2 == 0:
        curr_ptr.next = odd_head
    else:
        next_ptr.next = odd_head
        curr_ptr.next = None

    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("even_odd_list_merge.py",
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
