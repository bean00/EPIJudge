import collections

from test_framework import generic_test
from test_framework.test_failure import TestFailure

from collections import deque


class GraphVertex:
    def __init__(self, label):
        self.label = label
        self.edges = []


# Avg runtime 560 us; Median runtime 43 us
def clone_graph(graph):
    q = deque()
    created = set()
    vertices = {}

    start_label = graph.label
    start = GraphVertex(start_label)
    vertices[start_label] = start

    q.append(graph)
    created.add(start_label)

    while q:
        from_node = q.popleft()
        from_label = from_node.label

        for to_node in from_node.edges:
            to_label = to_node.label

            # create new node
            if to_label not in vertices:
                new_node = GraphVertex(to_label)
                vertices[to_label] = new_node

            # add edge from from_node to my_node (*Not to_node)
            my_node = vertices[to_label]
            vertices[from_label].edges.append(my_node)

            # add to_node to q, and to_label to created (if not in created)
            if to_label not in created:
                q.append(to_node)
                created.add(to_label)

    return start


def copy_labels(edges):
    return [e.label for e in edges]


def check_graph(node, graph):
    if node is None:
        raise TestFailure('Graph was not copied')

    vertex_set = set()
    q = collections.deque()
    q.append(node)
    vertex_set.add(node)
    while q:
        vertex = q.popleft()
        if vertex.label >= len(graph):
            raise TestFailure('Invalid vertex label')
        label1 = copy_labels(vertex.edges)
        label2 = copy_labels(graph[vertex.label].edges)
        if sorted(label1) != sorted(label2):
            raise TestFailure('Edges mismatch')
        for e in vertex.edges:
            if e not in vertex_set:
                vertex_set.add(e)
                q.append(e)


def clone_graph_test(k, edges):
    if k <= 0:
        raise RuntimeError('Invalid k value')
    graph = [GraphVertex(i) for i in range(k)]

    for (fr, to) in edges:
        if fr < 0 or fr >= k or to < 0 or to >= k:
            raise RuntimeError('Invalid vertex index')
        graph[fr].edges.append(graph[to])

    result = clone_graph(graph[0])
    check_graph(result, graph)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("graph_clone.py", 'graph_clone.tsv',
                                       clone_graph_test))
