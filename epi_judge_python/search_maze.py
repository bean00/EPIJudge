import collections
import copy
import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

from collections import defaultdict

WHITE, BLACK = range(2)  # WHITE = 0, BLACK = 1

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))


def search_maze(maze, s, e):
    # return search_maze_directly(maze, s, e)
    return search_maze_building_graph_first(maze, s, e)


def search_maze_directly(maze, s, e):
    # Perform DFS to find a feasible path
    def search_maze_helper(cur):
        # Checks cur is within maze and is a white pixel
        if not (0 <= cur.x < len(maze) and 0 <= cur.y < len(maze[cur.x])
                and maze[cur.x][cur.y] == WHITE):
            return False
        path.append(cur)
        maze[cur.x][cur.y] = BLACK
        if cur == e:
            return True

        if any(
            map(search_maze_helper,
                map(Coordinate, (cur.x - 1, cur.x + 1, cur.x, cur.x),
                    (cur.y, cur.y, cur.y - 1, cur.y + 1)))):
            return True

        # Cannot find a path, remove the entry added in path.append(cur)
        del path[-1]
        return False

    path = []
    search_maze_helper(s)
    return path


def search_maze_building_graph_first(maze, s, e):
    graph = build_graph(maze)
    path = find_path(graph, s, e)
    return path


def build_graph(maze):
    graph = defaultdict(list)
    num_rows, num_cols = len(maze), len(maze[0])

    for r in range(num_rows):
        for c in range(num_cols):
            from_val, from_cell = maze[r][c], (r, c)

            if from_val == 1:
                continue

            to_cells = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
            for to_cell in to_cells:
                to_row, to_col = to_cell[0], to_cell[1]

                if not 0 <= to_row <= num_rows - 1:
                    continue
                if not 0 <= to_col <= num_cols - 1:
                    continue

                to_val = maze[to_row][to_col]
                if from_val == to_val == 0:
                    graph[from_cell].append(to_cell)

    return graph


def find_path(graph, s, e):
    path = []
    find_path_using_dfs(graph, tuple(s), tuple(e), set(), path)

    return path


def find_path_using_dfs(graph, node, end, visited, path):
    visited.add(node)
    path.append(list(node))

    if node == end:
        return True

    are_neighbors_valid = []
    for neighbor in graph[node]:
        if neighbor not in visited:
            is_neighbor_valid = find_path_using_dfs(graph, neighbor, end, visited, path)
            are_neighbors_valid.append(is_neighbor_valid)

    if any(are_neighbors_valid):
        return True

    del path[-1]
    return False


def path_element_is_feasible(maze, prev, cur):
    if not ((0 <= cur.x < len(maze)) and
            (0 <= cur.y < len(maze[cur.x])) and maze[cur.x][cur.y] == WHITE):
        return False
    return cur == (prev.x + 1, prev.y) or \
           cur == (prev.x - 1, prev.y) or \
           cur == (prev.x, prev.y + 1) or \
           cur == (prev.x, prev.y - 1)


@enable_executor_hook
def search_maze_wrapper(executor, maze, s, e):
    s = Coordinate(*s)
    e = Coordinate(*e)
    cp = copy.deepcopy(maze)

    path = executor.run(functools.partial(search_maze, cp, s, e))

    if not path:
        return s == e

    if path[0] != s or path[-1] != e:
        raise TestFailure("Path doesn't lay between start and end points")

    for i in range(1, len(path)):
        if not path_element_is_feasible(maze, path[i - 1], path[i]):
            raise TestFailure("Path contains invalid segments")

    return True


if __name__ == '__main__':
    # exit(
    #     generic_test.generic_test_main("search_maze.py", 'search_maze.tsv',
    #                                    search_maze_wrapper))

    # WHITE = 0, BLACK = 1
    maze = [
        [0, 0, 0, 0],
        [1, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 0, 0, 0]
    ]
    s = [3, 0]
    e = [0, 3]

    # maze = [
    #     [0, 0, 1],
    #     [1, 0, 0]
    # ]
    # s = [0, 0]
    # e = [1, 2]

    print(search_maze(maze, s, e))
