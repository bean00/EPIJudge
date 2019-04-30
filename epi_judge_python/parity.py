from test_framework import generic_test


def parity(x):
    num_1_bits = count_num_1_bits(x)
    parity = num_1_bits % 2

    return parity


def count_num_1_bits(x):
    count = 0

    while x:
        if x & 1:
            count += 1

        x >>= 1

    return count


def parity_brute_force(x):
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result


def parity_drop_lowest_set_bit(x):
    result = 0
    while x:
        result ^= 1
        x &= x - 1
    return result


def parity_xor(x):
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 0x1


if __name__ == '__main__':
    # exit(generic_test.generic_test_main("parity.py", 'parity.tsv', parity_xor))
    # for i in range(11):
    #     print(parity(i))
    parity_xor(5)
