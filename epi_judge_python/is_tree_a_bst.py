from test_framework import generic_test


def is_binary_tree_bst(tree, low_range=float('-inf'), high_range=float('inf')):
    return use_interval(tree, low_range, high_range)


def use_interval(node, min, max):
    if node is None:
        return True

    if not min <= node.data <= max:
        return False

    is_left_valid = use_interval(node.left, min, node.data)
    is_right_valid = use_interval(node.right, node.data, max)

    return is_left_valid and is_right_valid


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_a_bst.py", 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
