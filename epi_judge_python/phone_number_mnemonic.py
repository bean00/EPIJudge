from test_framework import generic_test, test_utils

import copy

MAPPING = ('0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ')


def phone_mnemonic(phone_number):
    return my_solution(phone_number)


def my_solution(phone_number):
    def build_sequences(digits, sequence):
        if len(digits) == 0:
            seq_str = ''.join(sequence)
            sequences.append(seq_str)
        else:
            digit = int(digits[0])
            for char in MAPPING[digit]:
                seq_copy = copy.deepcopy(sequence)
                seq_copy.append(char)
                build_sequences(digits[1:], seq_copy)

    digits = list(phone_number)
    sequences = []
    build_sequences(digits, [])

    return sequences


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "phone_number_mnemonic.py",
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
