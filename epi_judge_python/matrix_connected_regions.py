from test_framework import generic_test


# Avg runtime 32 us; Median runtime 14 us
def flip_color(x, y, image):
    color = image[x][y]
    opposite_color = 1 - color
    r, c = len(image), len(image[0])

    flip_color_dfs(x, y, image, r, c, color, opposite_color)


def flip_color_dfs(x, y, image, r, c, color, opposite_color):
    image[x][y] = opposite_color  # mark node as visited (cell has 'opposite color')

    all_neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    valid_neighbors = [(x, y) for (x, y) in all_neighbors if (0 <= x <= r - 1) and (0 <= y <= c - 1)]

    for next_x, next_y in valid_neighbors:
        # if not visited (cell has 'color')
        if image[next_x][next_y] == color:
            flip_color_dfs(next_x, next_y, image, r, c, color, opposite_color)


def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("matrix_connected_regions.py",
                                       'painting.tsv', flip_color_wrapper))
