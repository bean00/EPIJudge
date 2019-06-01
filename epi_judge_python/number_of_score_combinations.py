from test_framework import generic_test


def num_combinations_for_final_score(final_score, individual_play_scores):
    # return calc_combos_for_each_score(final_score, individual_play_scores)
    return calc_combos_using_2D_table(final_score, individual_play_scores)


# Avg runtime 960 us; Median runtime 652 us
def calc_combos_using_2D_table(final_score, individual_play_scores):
    # One way to reach 0
    num_combinations_for_score = [[1] + [0] * final_score
                                  for _ in individual_play_scores]

    for i in range(len(individual_play_scores)):
        for j in range(1, final_score + 1):
            without_this_play = (
                num_combinations_for_score[i - 1][j]
                if i >= 1 else 0
            )
            with_this_play = (
                num_combinations_for_score[i][j - individual_play_scores[i]]
                if j >= individual_play_scores[i] else 0
            )
            num_combinations_for_score[i][j] = without_this_play + with_this_play

    return num_combinations_for_score[-1][-1]


# *Too slow! O(npc) (n - score, p - # plays, c - # combinations)
def calc_combos_for_each_score(final_score, individual_play_scores):
    sorted_play_scores = sorted(individual_play_scores)
    combos = [set() for _ in range(final_score + 1)]

    for score in range(1, final_score + 1):
        for play_score in sorted_play_scores:
            previous_score = score - play_score

            if previous_score < 0:
                continue

            if previous_score == 0:
                tup = build_single_play_tuple(score, sorted_play_scores)
                combos[score].add(tup)

            for tup in combos[previous_score]:
                arr = list(tup)
                for i, elem in enumerate(sorted_play_scores):
                    if elem == play_score:
                        arr[i] += 1

                updated_tup = tuple(arr)
                if updated_tup not in combos[score]:
                    combos[score].add(updated_tup)

    print(combos[final_score])
    total_num_combos = len(combos[final_score])
    return total_num_combos


def build_single_play_tuple(score, sorted_play_scores):
    arr = [0] * len(sorted_play_scores)

    for i, elem in enumerate(sorted_play_scores):
        if elem == score:
            arr[i] += 1

    return tuple(arr)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_score_combinations.py",
                                       "number_of_score_combinations.tsv",
                                       num_combinations_for_final_score))

    # final_score = 12
    # individual_play_scores = [2, 3, 7]
    # print(num_combinations_for_final_score(final_score, individual_play_scores))
