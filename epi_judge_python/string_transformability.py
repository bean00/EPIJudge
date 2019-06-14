from test_framework import generic_test

from collections import Counter
from collections import defaultdict
from collections import deque
from collections import namedtuple

import string


def transform_string(D, s, t):
    # return build_tree_then_find_depth(D, s, t)
    return try_all_string_transformations(D, s, t)
    # return try_all_string_transformations_original(D, s, t)


# Avg runtime 62 ms; Median runtime 13 ms
def try_all_string_transformations(D, s, t):
    Node = namedtuple('Node', ('string', 'level'))
    q = deque([Node(s, 0)])
    D.remove(s)  # mark s as visited

    while q:
        word, level = q.popleft()
        if word == t:
            return level

        for i in range(len(word)):
            for c in string.ascii_lowercase:
                new_word = word[:i] + c + word[i + 1:]
                if new_word in D:
                    D.remove(new_word)
                    q.append(Node(new_word, level + 1))

    return -1


def build_tree_then_find_depth(D, s, t):
    tree = defaultdict(list)
    D.remove(s)
    build_tree_of_possible_paths(s, D, tree)
    # print(tree)

    depth = find_depth_of_end(s, t, tree)
    return depth


def build_tree_of_possible_paths(start, dict, tree):
    children = []
    start_count = Counter(start)

    for word in dict:
        word_count = Counter(word)
        result = word_count - start_count
        result_has_one_letter = len(result) == sum(result.values()) == 1
        if result_has_one_letter:
            children.append(word)

    tree[start] = children

    for child in children:
        dict.remove(child)
        build_tree_of_possible_paths(child, dict, tree)


def find_depth_of_end(start, end, tree):
    curr_nodes = [start]
    depth = 0

    while curr_nodes:
        depth += 1
        curr_nodes = [
            child
            for curr in curr_nodes for child in tree[curr]
        ]
        if end in set(curr_nodes):
            return depth

    return -1


# Avg runtime 85 ms; Median runtime 17 ms
def try_all_string_transformations_original(D, s, t):
    StringWithDistance = namedtuple(
        'StringWithDistance', ('candidate_string', 'distance')
    )
    q = deque([StringWithDistance(s, 0)])
    D.remove(s)  # Marks s as visited by erasing it in D

    while q:
        f = q.popleft()
        # Returns if we find a match
        if f.candidate_string == t:
            return f.distance  # Number of steps reaches t

        # Tries all possible transformations of f.candidate_string
        for i in range(len(f.candidate_string)):
            for c in string.ascii_lowercase:  # Iterates through 'a' ~ 'z'
                cand = f.candidate_string[:i] + c + f.candidate_string[i + 1:]
                if cand in D:
                    D.remove(cand)
                    q.append(StringWithDistance(cand, f.distance + 1))
    return -1  # Cannot find a possible transformation


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("string_transformability.py",
                                       'string_transformability.tsv',
                                       transform_string))
