from test_framework import generic_test


def plus_one(A):
    i = len(A) - 1

    while A[i] == 9:
        A[i] = 0
        i -= 1

    if i < 0:
        A.append(0)
        A[0] = 1
    else:
        A[i] += 1

    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_increment.py",
                                       "int_as_array_increment.tsv", plus_one))
