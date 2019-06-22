from test_framework import generic_test

from collections import deque


def fill_surrounded_regions(board):
    process_boundary_white_nodes(board)
    return


def process_boundary_white_nodes(board):
    stay_white = set()
    num_rows, num_cols = len(board), len(board[0])
    white_boundary_nodes = []

    # get all boundary nodes that are white
    full_top_row = [(0, c) for c in range(num_cols)]
    full_bottom_row = [(num_rows - 1, c) for c in range(num_cols)]
    middle_left_col = [(r, 0) for r in range(1, num_rows - 2)]
    middle_right_col = [(r, num_cols - 1) for r in range(1, num_rows - 2)]

    for r, c in full_top_row + full_bottom_row + middle_left_col + middle_right_col:
        if board[r][c] == 'W':
            white_boundary_nodes.append((r, c))

    # create a q with the white boundary nodes
    q = deque(white_boundary_nodes)
    # create a set to track visited nodes
    visited = set(white_boundary_nodes)

    # while q is not empty
    while q:
        # pop node from q
        node = q.popleft()

        # add node to stay_white set
        stay_white.add(node)
        # add node to visited set
        visited.add(node)
        # get all neighbors that are white and not in the set
        r, c = node
        potential_neighbors = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
        for r, c in potential_neighbors:
            if (0 <= r <= num_rows - 1) and (0 <= c <= num_cols - 1) and board[r][c] == 'W' and (r, c) not in visited:
                # add neighbors to q
                q.append((r, c))
                # ? add node to visited?
                visited.add((r, c))

    # loop through all cells in board
    for r in range(num_rows):
        for c in range(num_cols):
            # any cell that is white and NOT in stay_white set, change color
            if board[r][c] == 'W' and (r, c) not in stay_white:
                board[r][c] = 'B'


def fill_surrounded_regions_wrapper(board):
    fill_surrounded_regions(board)
    return board


def print_2d_list(list):
    for row in list:
        print(row)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("matrix_enclosed_regions.py",
                                       'matrix_enclosed_regions.tsv',
                                       fill_surrounded_regions_wrapper))

    # board = [
    #     ['B', 'W', 'B', 'B', 'W'],
    #     ['W', 'W', 'B', 'W', 'B'],
    #     ['B', 'W', 'B', 'W', 'B'],
    #     ['B', 'B', 'W', 'W', 'B'],
    #     ['W', 'W', 'B', 'B', 'B']
    # ]
    # print_2d_list(fill_surrounded_regions_wrapper(board))
