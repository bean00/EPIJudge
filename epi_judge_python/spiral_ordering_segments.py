from test_framework import generic_test


def matrix_in_spiral_order(square_matrix):
    return move_in_one_of_four_directions(square_matrix)


# Avg runtime 621 us; Median runtime 515 us
def move_in_one_of_four_directions(square_matrix):
    if not square_matrix:
        return []

    direction = 'right'
    i = j = 0
    max_index = len(square_matrix) - 1
    visited = set()
    ordering = []

    is_next_cell_blocked = False

    while not is_next_cell_blocked:
        ordering.append(square_matrix[i][j])
        visited.add((i, j))
        new_i, new_j = i, j

        # try moving in 'direction'
        if direction == 'right':
            new_j = j + 1
        elif direction == 'down':
            new_i = i + 1
        elif direction == 'left':
            new_j = j - 1
        else:  # direction == 'up'
            new_i = i - 1

        # if move is blocked, try turning right
        is_next_cell_blocked = test_if_cell_is_blocked(new_i, new_j, max_index, visited)

        # try new move
        if is_next_cell_blocked:
            if direction == 'right':  # check 'down'
                new_i = i + 1
                new_j = j
                direction = 'down'
            elif direction == 'down':  # check 'left'
                new_j = j - 1
                new_i = i
                direction = 'left'
            elif direction == 'left':  # check 'up'
                new_i = i - 1
                new_j = j
                direction = 'up'
            else:  # direction == 'up'  # check 'right'
                new_j = j + 1
                new_i = i
                direction = 'right'

        i = new_i
        j = new_j
        is_next_cell_blocked = test_if_cell_is_blocked(i, j, max_index, visited)

    return ordering


def test_if_cell_is_blocked(i, j, max_index, visited):
    in_bounds = (0 <= i <= max_index) and (0 <= j <= max_index)
    not_visited = (i, j) not in visited

    return not (in_bounds and not_visited)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("spiral_ordering_segments.py",
                                       "spiral_ordering_segments.tsv",
                                       matrix_in_spiral_order))
