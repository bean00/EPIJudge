from test_framework import generic_test

from bst_node import BstNode


def rebuild_bst_from_preorder(preorder_sequence):
    # return my_solution(preorder_sequence)
    return author_solution(preorder_sequence)


# Avg runtime 402 us; Median runtime 43 us
def my_solution(preorder_sequence):
    bst = build_bst(preorder_sequence, 0, len(preorder_sequence))
    return bst


def build_bst(seq, start, end):
    if start == end:
        return None

    node = BstNode(seq[start])

    right = start
    while right < end and seq[right] <= seq[start]:
        right += 1

    node.left = build_bst(seq, start + 1, right)
    node.right = build_bst(seq, right, end)

    return node


# Avg runtime 284 us; Median runtime 40 us
def author_solution(preorder_sequence):
    def rebuild_bst_from_preorder_on_value_range(lower_bound, upper_bound):
        if root_idx[0] == len(preorder_sequence):
            return None

        root = preorder_sequence[root_idx[0]]
        if not lower_bound <= root <= upper_bound:
            return None
        root_idx[0] += 1
        # Note that rebuild_bst_from_preorder_on_value_range updates root_idx[0]
        # So the order of following two calls are critical
        left_subtree = rebuild_bst_from_preorder_on_value_range(
            lower_bound, root)
        right_subtree = rebuild_bst_from_preorder_on_value_range(
            root, upper_bound)
        return BstNode(root, left_subtree, right_subtree)

    root_idx = [0]  # Tracks current subtree
    return rebuild_bst_from_preorder_on_value_range(
        float('-inf'), float('inf'))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("bst_from_preorder.py",
                                       'bst_from_preorder.tsv',
                                       rebuild_bst_from_preorder))
