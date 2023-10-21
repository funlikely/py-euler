"""
    Coin Partitions


    Problem 78

    Let p(n) represent the number of different ways in which n coins can be separated into piles. For example,
    five coins can be separated into piles in exactly seven different ways, so p(5) = 7

    OOOOO
    OOOO   O
    OOO   OO
    OOO   O   O
    OO   OO   O
    OO   O   O   O
    O   O   O   O   O

    Find the least value of n
    for which p(n) is divisible by one million.

    Let's define p(n) = P(n,n) where P(n,m) is the number of ways to partition n coins using a maximum
    partition size of m.

    Specially define P(n,0) = 1

    Some examples:
    P(n,0) = 1
    P(n,1) = 1

    P(n,m) = sum(sum(P(n-i, min(i, n-i)), for j from __ to __),  for i from n down to 0)

    p(7) = P(7,7)
    =  P(0,0)
     + P(1,1)
     + P(2,2)
     + P(3,3)
     + P(4,3) + P(1,1)
     + P(5,2) + P(3,2) + P(1,1)
     + P(6,1)
     + P(7,0)

    P(4,3)
    =  xxx x, xx xx, xx x x, x x x x
    =  P(1,1)
     + P(4,2)
     + P(4,1)

    P(5,2)
    =  xx xx x, xx x x x, x x x x x
    = P(1,1) + P(3,1) + P(1,1)
"""
import math


debug = True
indent = ""


def p_deprecated(n, m):
    global indent
    print(f'{indent}p({n}, {m})')
    if cache[n][m] != 0:
        return cache[n][m]
    if n < 2 or m < 2:
        cache[n][m] = 1
        return 1
    result = 0
    for i in range(n-1):
        k = n - i
        cycles = math.floor(n/k)
        for a in range(1, cycles + 1):
            indent += "  "
            reduction = n-a*k
            if cycles == 1:
                partition_max_size = reduction
            else:
                partition_max_size = min(reduction, k - 1)
            result += p_deprecated(reduction, partition_max_size)
            indent = indent[:-2]
    # result += p(n, 1)
    cache[n][m] = result
    return result


def p(n, k):
    """New version, using a combinatorics textbook, since my-y-y-y-y version was failing pretty hard"""
    if n < 0 or k < 0:
        return 0
    if n == 0 or k == 0:
        return cache[n][k]
    if cache[n][k] != 0:
        return cache[n][k]
    if k == 1 or n == k or k == n-1:
        cache[n][k] = 1
        return 1

    result = 0
    result += p(n-1, k-1)
    result += p(max(0, n-k), k)

    return result


def partitions(n):
    result = 0
    for k in range(1, n+1):
        result += p(n, k)
    return result


def get_number_of_partitions(n):
    global cache
    max_size = 46
    cache = [[0 for j in range(max_size)] for i in range(max_size)]

    if debug:
        for i in range(44):
            print(f'(p({i}) = {partitions(i)}')
        test_val = p_deprecated(5, 5)
    if debug:
        for row in cache:
            print(f'{row}')

    result = partitions(n)
    return result


def get_answer():
    return get_number_of_partitions(7)


def main():
    answer = get_answer()
    print(f"The Answer to Project Euler 078 is {answer}")

    # The Answer to Project Euler 078 is


if __name__ == "__main__":
    main()
