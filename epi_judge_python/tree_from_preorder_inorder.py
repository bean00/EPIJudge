from test_framework import generic_test

from binary_tree_node import BinaryTreeNode


def binary_tree_from_preorder_inorder(preorder, inorder):
    # return my_solution(preorder, inorder)
    return author_solution(preorder, inorder)


def author_solution(preorder, inorder):
    node_to_inorder_idx = {data: i for i, data in enumerate(inorder)}

    # Builds the subtree with preorder[preorder_start:preorder_end] and
    # inorder[inorder_start:inorder_end]
    def binary_tree_helper(preorder_start, preorder_end, inorder_start, inorder_end):
        if preorder_end <= preorder_start or inorder_end <= inorder_start:
            return None

        root_inorder_idx = node_to_inorder_idx[preorder[preorder_start]]
        left_subtree_size = root_inorder_idx - inorder_start
        return BinaryTreeNode(
            preorder[preorder_start],
            # Recursively builds the left subtree
            binary_tree_helper(
                preorder_start + 1, preorder_start + 1 + left_subtree_size,
                inorder_start, root_inorder_idx),
            # Recursively builds the right subtree
            binary_tree_helper(
                preorder_start + 1 + left_subtree_size, preorder_end,
                root_inorder_idx + 1, inorder_end))

    return binary_tree_helper(0, len(preorder), 0, len(inorder))


def my_solution(preorder, inorder):
    root = BinaryTreeNode()
    build_tree(preorder, inorder, root, 0, 0, len(inorder) - 1)
    return root


def build_tree(preorder, inorder, root, pre_idx, left, right):
    root_data = preorder[pre_idx]
    root.data = root_data

    in_sub_arr = inorder[left:right + 1]
    in_idx = in_sub_arr.index(root_data)

    if in_idx > left:
        node = BinaryTreeNode()
        root.left = node
        build_tree(preorder, inorder, root.left, pre_idx + 1, left, in_idx - 1)

    if in_idx < right:
        node = BinaryTreeNode()
        root.right = node
        build_tree(preorder, inorder, root.right, pre_idx + 1, in_idx + 1, right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_from_preorder_inorder.py",
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
