import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

NUM_PEGS = 3


def compute_tower_hanoi(num_rings):
    moves = []

    move_n_rings(moves, num_rings, 0, 2)

    return moves


def move_n_rings(moves, ring_num, from_peg, to_peg):
    if ring_num == 1:
        move_ring(moves, from_peg, to_peg)
    else:
        other_peg = 3 - from_peg - to_peg
        move_n_rings(moves, ring_num - 1, from_peg, other_peg)
        move_ring(moves, from_peg, to_peg)
        move_n_rings(moves, ring_num - 1, other_peg, to_peg)


def move_ring(moves, from_peg, to_peg):
    moves.append((from_peg, to_peg))


@enable_executor_hook
def compute_tower_hanoi_wrapper(executor, num_rings):
    pegs = [list(reversed(range(1, num_rings + 1)))] + [[] for _ in range(
        1, NUM_PEGS)]

    result = executor.run(functools.partial(compute_tower_hanoi, num_rings))

    for from_peg, to_peg in result:
        if pegs[to_peg] and pegs[from_peg][-1] >= pegs[to_peg][-1]:
            raise TestFailure("Illegal move from {} to {}".format(
                pegs[from_peg][-1], pegs[to_peg][-1]))
        pegs[to_peg].append(pegs[from_peg].pop())
    expected_pegs1 = [[], [], list(reversed(range(1, num_rings + 1)))]
    expected_pegs2 = [[], list(reversed(range(1, num_rings + 1))), []]
    if pegs not in (expected_pegs1, expected_pegs2):
        raise TestFailure("Pegs doesn't place in the right configuration")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("hanoi.py", 'hanoi.tsv',
                                       compute_tower_hanoi_wrapper))
