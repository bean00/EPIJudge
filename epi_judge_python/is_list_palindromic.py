from test_framework import generic_test


def is_linked_list_a_palindrome(L):
    return my_solution(L)


def my_solution(L):
    if not L or not L.next:
        return True

    mid = find_middle(L)

    reversed_half = reverse_list(mid.next)

    list_are_equal = are_lists_equal(L, reversed_half)
    return list_are_equal


def find_middle(L):
    fast = slow = L

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def reverse_list(head):
    prev = None
    curr = head

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    return prev


def are_lists_equal(l1, l2):
    # *Note: l1 includes l2, so check if l2 still exists
    while l2:
        if l1.data != l2.data:
            return False
        l1, l2 = l1.next, l2.next

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_list_palindromic.py",
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
