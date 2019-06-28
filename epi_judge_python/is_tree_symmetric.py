from test_framework import generic_test


def is_symmetric(tree):
    if not tree:
        return True

    is_symmetric = subtrees_equal(tree.left, tree.right)
    return is_symmetric


def subtrees_equal(left, right):
    if not left and not right:  # or, 'if not left and not right'
        return True
    if (not left) or (not right) or (left.data != right.data):
        return False

    is_outside_symmetric = subtrees_equal(left.left, right.right)
    is_inside_symmetric = subtrees_equal(left.right, right.left)

    return is_outside_symmetric and is_inside_symmetric


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_symmetric.py",
                                       'is_tree_symmetric.tsv', is_symmetric))
