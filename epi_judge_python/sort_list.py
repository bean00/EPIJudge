from test_framework import generic_test

from list_node import ListNode


def stable_sort_list(L):
    # Base cases: L is empty or a single node, nothing to do
    if not L or not L.next:
        return L

    pre_slow, slow, fast = None, L, L

    while fast and fast.next:
        pre_slow = slow
        slow, fast = slow.next, fast.next.next

    pre_slow.next = None  # Splits the list into two equal-sized lists

    left = stable_sort_list(L)
    right = stable_sort_list(slow)
    return merge_two_sorted_lists(left, right)


def merge_two_sorted_lists(L1, L2):
    # Creates a placeholder for the result
    dummy_head = tail = ListNode()

    while L1 and L2:
        if L1.data < L2.data:
            tail.next, L1 = L1, L1.next
        else:
            tail.next, L2 = L2, L2.next
        tail = tail.next

    # Appends the remaining nodes of L1 or L2
    tail.next = L1 or L2
    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sort_list.py", 'sort_list.tsv',
                                       stable_sort_list))
