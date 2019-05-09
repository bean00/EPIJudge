from test_framework import generic_test
from test_framework.test_failure import TestFailure


# My initial implementation: avg runtime 149 us; median runtime 20 us
class Stack:
    def __init__(self):
        self.stack = []
        self.max_list = []

    def empty(self):
        is_empty = len(self.stack) == 0
        return is_empty

    def max(self):
        max_item = self.max_list[-1]
        return max_item

    def pop(self):
        self.max_list.pop()

        top_item = self.stack.pop()
        return top_item

    def push(self, item):
        self.stack.append(item)

        if self.max_list:
            next_max = max(item, self.max())
            self.max_list.append(next_max)
        else:
            self.max_list.append(item)


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure(
                        "Pop: expected " + str(arg) + ", got " + str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure(
                        "Max: expected " + str(arg) + ", got " + str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure(
                        "Empty: expected " + str(arg) + ", got " + str(result))
            else:
                raise RuntimeError("Unsupported stack operation: " + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("stack_with_max.py",
                                       'stack_with_max.tsv', stack_tester))
