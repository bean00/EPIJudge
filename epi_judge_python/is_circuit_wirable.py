import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

from collections import deque

WHITE, BLACK, UNSET = 1, -1, 0


class GraphVertex:
    def __init__(self):
        self.d = -1
        self.edges = []
        self.color = UNSET


def is_any_placement_feasible(graph):
    def bfs(start_node):
        start_node.color = WHITE
        q = deque([start_node])
        while q:
            node = q.popleft()
            opposite_color = node.color * -1  # (1 * -1 = -1); (-1 * -1 = 1)
            for neighbor in node.edges:
                if neighbor.color == node.color:
                    return False
                elif neighbor.color == UNSET:
                    neighbor.color = opposite_color
                    q.append(neighbor)
        return True

    results = [bfs(node) for node in graph if node.color == UNSET]
    return all(results)


@enable_executor_hook
def is_any_placement_feasible_wrapper(executor, k, edges):
    if k <= 0:
        raise RuntimeError('Invalid k value')
    graph = [GraphVertex() for _ in range(k)]

    for (fr, to) in edges:
        if fr < 0 or fr >= k or to < 0 or to >= k:
            raise RuntimeError('Invalid vertex index')
        graph[fr].edges.append(graph[to])

    return executor.run(functools.partial(is_any_placement_feasible, graph))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_circuit_wirable.py",
                                       'is_circuit_wirable.tsv',
                                       is_any_placement_feasible_wrapper))
