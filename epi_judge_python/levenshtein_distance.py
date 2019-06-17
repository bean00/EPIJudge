from test_framework import generic_test


# Avg runtime 980 us; Median runtime 450 us
def levenshtein_distance(A, B):
    len_a, len_b = len(A), len(B)

    arr = [[0] * (len_b + 1) for _ in range(len_a + 1)]

    for i in range(len_a + 1):
        arr[i][0] = i
    for j in range(len_b + 1):
        arr[0][j] = j

    for i in range(1, len_a + 1):
        for j in range(1, len_b + 1):
            subs_cost = 0 if A[i - 1] == B[j - 1] else 1
            min_dist = min(
                arr[i - 1][j - 1] + subs_cost,  # substitute
                arr[i][j - 1] + 1,              # insert
                arr[i - 1][j] + 1               # delete
            )
            arr[i][j] = min_dist

    return arr[len_a][len_b]


def print_2d_list(li):
    for row in li:
        print(row)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("levenshtein_distance.py",
                                       "levenshtein_distance.tsv",
                                       levenshtein_distance))
