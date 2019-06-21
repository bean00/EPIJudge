from test_framework import generic_test


def find_first_greater_than_k(tree, k):
    # return use_recursion(tree, k)
    return use_iteration(tree, k)


def use_recursion(tree, k):
    result = find_greater_than_k(tree, k, None)
    return result


def find_greater_than_k(node, k, greater_key):
    if node is None:
        return greater_key

    if node.data > k:
        greater_key = node
        return find_greater_than_k(node.left, k, greater_key)
    else:  # node.data <= k
        return find_greater_than_k(node.right, k, greater_key)


def use_iteration(tree, k):
    subtree, first_so_far = tree, None
    while subtree:
        if subtree.data > k:
            first_so_far = subtree
            subtree = subtree.left
        else:  # Root and all keys in left subtree are <= k, so skip them
            subtree = subtree.right
    return first_so_far


def find_first_greater_than_k_wrapper(tree, k):
    result = find_first_greater_than_k(tree, k)
    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_first_greater_value_in_bst.py",
                                       'search_first_greater_value_in_bst.tsv',
                                       find_first_greater_than_k_wrapper))
