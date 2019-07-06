import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))

# Endpoint is a tuple (start_time, 0) or (end_time, 1) so that if times
# are equal, start_time comes first
Endpoint = collections.namedtuple('Endpoint', ('time', 'is_start'))


def find_max_simultaneous_events(A):
    # return my_solution(A)
    return author_solution(A)


def my_solution(A):
    max_finish_event = max(A, key=lambda x: x.finish)
    max_finish = max_finish_event.finish

    net_start = [0] * (max_finish + 1)
    for event in A:
        start = event.start
        finish = event.finish
        net_start[start] += 1
        net_start[finish] -= 1

    num_events = max_num_events = 0
    for net_val in net_start:
        num_events += net_val
        max_num_events = max(num_events, max_num_events)

    # print(net_start)
    return max_num_events


def author_solution(A):
    # Builds an array of all endpoints
    E = [
        p
        for event in A for p in (Endpoint(event.start, True),
                                 Endpoint(event.finish, False))
    ]
    # Sorts the endpoint array according to the time, breaking ties by putting
    # start times before end times
    E.sort(key=lambda e: (e.time, not e.is_start))

    # Track the number of simultaneous events, record the maximum number of
    # simultaneous events
    max_num_simultaneous_events, num_simultaneous_events = 0, 0
    for e in E:
        if e.is_start:
            num_simultaneous_events += 1
            max_num_simultaneous_events = max(num_simultaneous_events,
                                              max_num_simultaneous_events)
        else:
            num_simultaneous_events -= 1
    return max_num_simultaneous_events


@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(
        functools.partial(find_max_simultaneous_events, events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("calendar_rendering.py",
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))
