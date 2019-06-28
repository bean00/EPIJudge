from test_framework import generic_test
from test_framework.test_failure import TestFailure


# Avg runtime 500 us; Median runtime 29 us
class Queue:
    def __init__(self, capacity):
        self.queue = []
        self.num_elem = 0

    def enqueue(self, x):
        self.queue.append(x)
        self.num_elem += 1

    def dequeue(self):
        first_elem = self.queue[0]
        self.queue = self.queue[1:]
        self.num_elem -= 1
        return first_elem

    def size(self):
        return self.num_elem


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure(
                    "Dequeue: expected " + str(arg) + ", got " + str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure(
                    "Size: expected " + str(arg) + ", got " + str(result))
        else:
            raise RuntimeError("Unsupported queue operation: " + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("circular_queue.py",
                                       'circular_queue.tsv', queue_tester))
