from test_framework import generic_test


def longest_nondecreasing_subsequence_length(A):
    # return author_solution(A)
    return my_solution(A)


# Avg runtime 21 us; Median runtime 8 us
# Compared to author: Avg 13X faster; Med 7X faster
def my_solution(A):
    result = []

    for elem in A:
        if not result or elem >= result[-1]:
            result.append(elem)
        else:
            i = len(result) - 1
            while i >= 0 and elem < result[i]:
                i -= 1
            result[i + 1] = elem

    length = len(result)
    return length


# Avg runtime 274 us; Median runtime 52 us
def author_solution(A):
    # max_length[i] holds the length of the longest nondecreasing subsequence
    # of A[:i + 1]
    max_length = [1] * len(A)
    for i in range(1, len(A)):
        max_length[i] = max(1 + max(
            (max_length[j] for j in range(i) if A[i] >= A[j]), default=0),
                            max_length[i])
    return max(max_length)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "longest_nondecreasing_subsequence.py",
            'longest_nondecreasing_subsequence.tsv',
            longest_nondecreasing_subsequence_length))
