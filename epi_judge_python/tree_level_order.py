from test_framework import generic_test

from collections import deque


def binary_tree_depth_order(tree):
    # return single_queue_with_node_and_depth(tree)
    return use_new_queue_for_each_level(tree)


# Avg runtime 19 us; Median runtime 3 us
def single_queue_with_node_and_depth(tree):
    if not tree:
        return []
    queue, nodes, level_nodes = deque(), [], []
    curr_depth = 0

    queue.append((tree, curr_depth))
    while queue:
        node, depth = queue.popleft()
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))

        if depth > curr_depth:
            nodes.append(level_nodes)
            level_nodes = []
            curr_depth += 1

        level_nodes.append(node.data)

    nodes.append(level_nodes)

    return nodes


# Avg runtime 13 us; Median runtime 4 us
def use_new_queue_for_each_level(tree):
    result = []
    if not tree:
        return result

    curr_depth_nodes = [tree]
    while curr_depth_nodes:
        result.append([curr.data for curr in curr_depth_nodes])
        curr_depth_nodes = [
            child
            for curr in curr_depth_nodes for child in (curr.left, curr.right)
            if child
        ]

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_level_order.py",
                                       "tree_level_order.tsv",
                                       binary_tree_depth_order))
