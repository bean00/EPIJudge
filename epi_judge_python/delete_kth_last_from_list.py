from test_framework import generic_test

from list_node import ListNode


def remove_kth_last(L, k):
    p1 = p2 = dummy_head = ListNode(0, L)
    p1 = p1.next

    for _ in range(k):
        p1 = p1.next

    while p1:
        p1 = p1.next
        p2 = p2.next

    p2.next = p2.next.next

    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("delete_kth_last_from_list.py",
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
