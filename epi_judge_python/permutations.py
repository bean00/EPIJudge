from test_framework import generic_test, test_utils


def permutations(A):
    # return my_solution(A)
    return author_solution(A)


def author_solution(A):
    def directed_permutations(i):
        if i == len(A) - 1:
            result.append(A.copy())
            return

        # Try every possibility for A[i]
        for j in range(i, len(A)):
            A[i], A[j] = A[j], A[i]
            # Generate all permutations for A[i + 1:]
            directed_permutations(i + 1)
            A[i], A[j] = A[j], A[i]

    result = []
    directed_permutations(0)
    return result


def my_solution(A):
    return permutations_helper(A, [])


def permutations_helper(A, answer):
    if len(A) == 1:
        return [A]

    for i in range(len(A)):
        curr = A[i]
        sub_arr = A[:i] + A[i + 1:]
        tmp_answer = permutations_helper(sub_arr, answer)
        for arr in tmp_answer:
            answer.append([curr] + arr)

    return answer


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("permutations.py", 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
