from test_framework import generic_test

from collections import deque


def evaluate(expression):
    expression = expression.split(',')
    stack = deque()
    operators = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: int(x / y)
    }

    for elem in expression:
        if elem in operators:
            right_val = stack.pop()
            left_val = stack.pop()
            result = operators[elem](left_val, right_val)
            stack.append(result)
        else:
            stack.append(int(elem))

    final_result = stack.pop()
    return final_result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("evaluate_rpn.py", 'evaluate_rpn.tsv',
                                       evaluate))
