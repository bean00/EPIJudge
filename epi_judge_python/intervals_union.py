import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Endpoint = collections.namedtuple('Endpoint', ('is_closed', 'val'))

Interval = collections.namedtuple('Interval', ('left', 'right'))


def union_of_intervals(intervals):
    # return my_solution(intervals)
    return author_solution(intervals)


def author_solution(intervals):
    # Empty input
    if not intervals:
        return []

    # Sort intervals according to left endpoints of intervals
    intervals.sort(key=lambda i: (i.left.val, not i.left.is_closed))
    result = [intervals[0]]

    for i in intervals:
        recent = result[-1]
        if (i.left.val < recent.right.val or
                (i.left.val == recent.right.val and (i.left.is_closed or recent.right.is_closed))):
            if (i.right.val > recent.right.val or
                    (i.right.val == recent.right.val and i.right.is_closed)):
                result[-1] = Interval(recent.left, i.right)
        else:
            result.append(i)

    return result


def my_solution(intervals):
    intervals.sort(key=lambda x: x.left.val)  # sort left-closed first?
    # intervals.sort(key=lambda x: (x.left.val, 1 - x.left.is_closed))
    # print_intervals(intervals)
    result = []

    for interval in intervals:
        # get recently added 'recent' (result[-1]?)
        recent = result[-1]  # handle index error when result is empty?
        # if recent doesn't intersect with interval
        intersect = recent.right.val > interval.left.val
        endpoints_intersect = (recent.left.val == interval.left.val and recent.left.is_closed) or\
                              (recent.right.val == interval.right.val and (recent.right.is_closed or
                               interval.right.is_closed))
            # add interval to result
        # else # recent intersects with interval
            # update recent to be the union with interval

    return result


def print_intervals(intervals):
    for interval in intervals:
        print((interval.left.val, interval.left.is_closed), (interval.right.val, interval.right.is_closed))


@enable_executor_hook
def union_of_intervals_wrapper(executor, intervals):
    intervals = [
        Interval(Endpoint(x[1], x[0]), Endpoint(x[3], x[2])) for x in intervals
    ]

    result = executor.run(functools.partial(union_of_intervals, intervals))

    return [(i.left.val, i.left.is_closed, i.right.val, i.right.is_closed)
            for i in result]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("intervals_union.py",
                                       "intervals_union.tsv",
                                       union_of_intervals_wrapper))
