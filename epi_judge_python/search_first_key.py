from test_framework import generic_test


def search_first_of_k(A, k):
    # return find_k_then_search_left(A, k)
    return find_first_k_using_interval(A, k)


# *Solution from book that I redid myself
# Avg runtime 2 us; Median runtime 2 us
def find_first_k_using_interval(A, k):
    left, right, result = 0, len(A) - 1, -1
    # A[left:right + 1] is the candidate set

    while left <= right:
        mid = (left + right) // 2
        if A[mid] > k:
            right = mid - 1
        elif A[mid] == k:
            result = mid
            right = mid - 1  # Nothing to the right of mid can be solution
        else:  # A[mid] < k
            left = mid + 1

    return result


# Avg runtime 2 us; Median runtime 2 us
def find_k_then_search_left(A, k):
    left, right = 0, len(A) - 1
    k_i = None

    while left <= right:
        mid = (left + right) // 2
        if A[mid] == k:
            k_i = mid
            break
        elif A[mid] < k:
            left = mid + 1
        else:  # A[mid] > k
            right = mid - 1

    if k_i is None:
        return -1

    while left <= right:
        mid = (left + right) // 2
        if A[mid] == k:
            k_i = mid
            right = mid - 1
        else:  # A[mid] < k
            left = mid + 1

    return k_i


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_first_key.py", 'search_first_key.tsv', search_first_of_k))

    # A = [1, 1, 2, 3, 4, 5, 6, 7]
    # print(search_first_of_k(A, 1))
