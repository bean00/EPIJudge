from test_framework import generic_test

from collections import deque


def shortest_equivalent_path(path):
    # return my_solution(path)
    return author_solution(path)


def author_solution(path):
    if not path:
        raise ValueError('Empty string is not a valid path.')

    path_names = []  # Uses list as a stack
    # Special case: starts with '/', which is an absolute path
    if path[0] == '/':
        path_names.append('/')

    for token in (token for token in path.split('/')
                  if token not in ['.', '']):
        if token == '..':
            if not path_names or path_names[-1] == '..':
                path_names.append(token)
            else:
                if path_names[-1] == '/':
                    raise ValueError('Path error')
                path_names.pop()
        else:  # Must be a name
            path_names.append(token)

    result = '/'.join(path_names)
    return result[result.startswith('//'):]  # Avoid starting '//'


def my_solution(path):
    first_char = ''
    if path[0] == '/':
        first_char = '/'

    dirs = path.split('/')
    d = deque()

    for dir in dirs:
        if not d and dir == '..':
            d.append(dir)
        elif dir == '..':
            d.pop()
        elif dir and dir != '.':
            d.append(dir)

    new_dirs = list(d)
    short_path = first_char + '/'.join(new_dirs)

    return short_path


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("directory_path_normalization.py",
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))
