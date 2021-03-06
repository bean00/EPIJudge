from test_framework import generic_test


def has_three_sum(A, t):
    A.sort()

    # Finds if the sum of two numbers in A equals to t - a
    return any(has_two_sun(A, t - a) for a in A)


def has_two_sun(A, t):
    i, j = 0, len(A) - 1

    while i <= j:
        if A[i] + A[j] == t:
            return True
        elif A[i] + A[j] < t:
            i += 1
        else:  # A[i] + A[j] > t
            j -= 1

    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("three_sum.py", "three_sum.tsv",
                                       has_three_sum))
