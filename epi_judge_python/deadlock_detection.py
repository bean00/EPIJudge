import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class GraphVertex:
    WHITE, GRAY, BLACK = range(3)

    def __init__(self):
        self.status = 'unvisited'  # for my solution
        self.color = GraphVertex.WHITE  # for author solution
        self.edges = []


def is_deadlocked(graph):
    # return my_solution(graph)
    return author_solution(graph)


# Avg runtime 16 us; Median runtime 11 us
def my_solution(graph):
    has_cycle_results = [has_cycle(node) for node in graph]
    return any(has_cycle_results)


def has_cycle(node):
    if node.status == 'processed' or node.status == 'discovered':
        return False
    if node.status == 'unvisited':
        node.status = 'discovered'

    neighbors = node.edges
    if len(neighbors) == 0:
        node.status = 'processed'
        return False

    neighbors_have_cycle = []
    for neighbor in neighbors:
        if neighbor.status == 'discovered':
            return True
        has_cycle_result = has_cycle(neighbor)
        neighbors_have_cycle.append(has_cycle_result)

    return any(neighbors_have_cycle)


# Avg runtime 23 us; Median runtime 13 us
def author_solution(graph):
    def has_cycle(cur):
        # Visiting a gray vertex means a cycle
        if cur.color == GraphVertex.GRAY:
            return True

        cur.color = GraphVertex.GRAY  # Marks current vertex as a gray one
        # Traverse the neighbor vertices
        if any(next.color != GraphVertex.BLACK and has_cycle(next)
               for next in cur.edges):
            return True
        cur.color = GraphVertex.BLACK  # Marks current vertex as black
        return False

    return any(vertex.color == GraphVertex.WHITE and has_cycle(vertex)
               for vertex in graph)


@enable_executor_hook
def is_deadlocked_wrapper(executor, num_nodes, edges):
    if num_nodes <= 0:
        raise RuntimeError('Invalid num_nodes value')
    graph = [GraphVertex() for _ in range(num_nodes)]

    for (fr, to) in edges:
        if fr < 0 or fr >= num_nodes or to < 0 or to >= num_nodes:
            raise RuntimeError('Invalid vertex index')
        graph[fr].edges.append(graph[to])

    return executor.run(functools.partial(is_deadlocked, graph))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("deadlock_detection.py",
                                       'deadlock_detection.tsv',
                                       is_deadlocked_wrapper))
