from test_framework import generic_test, test_utils


def find_k_largest_in_bst(tree, k):
    largest_elements = []
    add_elements(tree, k, largest_elements)

    return largest_elements


def add_elements(node, k, largest_elements):
    # Perform reverse in-order traversal
    if node and len(largest_elements) < k:
        add_elements(node.right, k, largest_elements)
        if len(largest_elements) < k:
            largest_elements.append(node.data)
            add_elements(node.left, k, largest_elements)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "k_largest_values_in_bst.py", 'k_largest_values_in_bst.tsv',
            find_k_largest_in_bst, test_utils.unordered_compare))
