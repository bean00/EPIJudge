from test_framework import generic_test


def zipping_linked_list(L):
    return author_solution(L)


def author_solution(L):
    if not L or not L.next:
        return L

    # Finds the second half of L
    slow = fast = L
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next

    first_half_head = L
    second_half_head = slow.next
    slow.next = None  # Splits the list into two lists

    second_half_head = reverse_linked_list(second_half_head)

    # Interleave the first half and the reversed of the second half
    first_half_iter, second_half_iter = first_half_head, second_half_head
    while second_half_iter:
        second_half_iter.next, first_half_iter.next, second_half_iter = (
            first_half_iter.next, second_half_iter, second_half_iter.next)
        first_half_iter = first_half_iter.next.next

    return first_half_head


def reverse_linked_list(L):
    prev = None
    curr = L

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    return prev


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("zip_list.py", 'zip_list.tsv',
                                       zipping_linked_list))
