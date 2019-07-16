from test_framework import generic_test

from collections import deque


# Using a deque for queue
# - Avg runtime 94 us; Median runtime 24 us
# Using 2 stacks for queue
# - Avg runtime 106 us; Median runtime 35 us
class Queue:
    def __init__(self):
        self.insert = deque()
        self.remove = deque()

    def enqueue(self, x):
        self.insert.append(x)

    def dequeue(self):
        if not self.remove:
            while self.insert:
                elem = self.insert.pop()
                self.remove.append(elem)
        return self.remove.pop()


def queue_tester(ops):
    from test_framework.test_failure import TestFailure

    try:
        q = Queue()

        for (op, arg) in ops:
            if op == 'Queue':
                q = Queue()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure("Dequeue: expected " + str(arg) +
                                      ", got " + str(result))
            else:
                raise RuntimeError("Unsupported queue operation: " + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("queue_from_stacks.py",
                                       'queue_from_stacks.tsv', queue_tester))
