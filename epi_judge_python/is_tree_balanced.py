from collections import namedtuple
from test_framework import generic_test


def is_balanced_binary_tree(tree):
    # return compare_heights(tree)
    return use_balanced_and_height(tree)


# Avg runtime 94 us; Median runtime 68 us
def use_balanced_and_height(tree):
    BalancedStatusWithHeight = namedtuple(
        'BalancedStatusWithHeight', ('balanced', 'height'))

    # First value of the return value indicates if tree is balanced, and if
    # balanced the second value of the return value is the height of tree
    def check_balanced(tree):
        if not tree:
            return BalancedStatusWithHeight(True, -1)

        left_result = check_balanced(tree.left)
        if not left_result.balanced:
            # Left subtree is not balanced
            return BalancedStatusWithHeight(False, 0)

        right_result = check_balanced(tree.right)
        if not right_result.balanced:
            # Right subtree is not balanced
            return BalancedStatusWithHeight(False, 0)

        is_balanced = abs(left_result.height - right_result.height) <= 1
        height = max(left_result.height, right_result.height) + 1
        return BalancedStatusWithHeight(is_balanced, height)

    return check_balanced(tree).balanced


# Avg runtime 138 us; Median runtime 6 us
def compare_heights(tree):
    if not tree:
        return True

    height_left = get_height(tree.left)
    height_right = get_height(tree.right)

    if abs(height_right - height_left) > 1:
        return False

    left_balanced = compare_heights(tree.left)
    right_balanced = compare_heights(tree.right)

    return left_balanced and right_balanced


def get_height(node):
    if node is None:
        return 0

    height_left = get_height(node.left) + 1
    height_right = get_height(node.right) + 1

    return max(height_left, height_right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_balanced.py",
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
