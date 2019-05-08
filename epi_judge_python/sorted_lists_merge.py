from list_node import ListNode
from test_framework import generic_test


def merge_two_sorted_lists(L1, L2):
    # return my_solution(L1, L2)
    return author_solution(L1, L2)


# Avg runtime: 20 us, Median runtime: 7 us
def my_solution(L1, L2):
    if not L2:
        return L1
    if not L1:
        return L2

    main = L1 if L1.data <= L2.data else L2
    other = L2 if L1.data <= L2.data else L1
    final_list = main  # save a ptr to the head of main

    while other:
        if not main.next:
            main.next = other
            break
        elif main.data <= other.data <= main.next.data:
            next_other = other.next

            other.next = main.next
            main.next = other

            main = main.next
            other = next_other
        else:  # other.data > main.next.data
            main = main.next

    return final_list


# Avg runtime: 14 us; Median runtime 6 us
def author_solution(L1, L2):
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
        generic_test.generic_test_main("sorted_lists_merge.py",
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
