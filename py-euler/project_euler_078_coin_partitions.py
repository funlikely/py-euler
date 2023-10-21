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
cache = []
partitions_cache = []


def p_deprecated(n, m):
    global indent
    global cache
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
    global cache
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
    cache[n][k] = result

    return result


def partitions(n):
    global partitions_cache
    result = 0
    for k in range(1, n+1):
        if partitions_cache[n][k] == 0:
            partitions_cache[n][k] = p(n, k) % 10000000
        result += partitions_cache[n][k]
        result = result % 10000000
    partitions_cache[n][n] = result
    return result


def get_answer():
    global cache
    global partitions_cache
    max_size = 10000
    cache = [[0 for j in range(max_size)] for i in range(max_size)]
    partitions_cache = [[0 for j in range(max_size)] for i in range(max_size)]

    for i in range(max_size - 2):
        result = partitions(i)
        print(f'p({i}) = {result}')

        if i > 20 and result % 1000000 == 0:
            return i
        if debug and i > 20 and result % 100000 == 0:
            print(f'p({i}) = {result}, divisible by 10^5')
        elif debug and i > 20 and result % 10000 == 0:
            print(f'p({i}) = {result}, divisible by 10^4')

    if False and debug:
        for row in cache:
            print(f'{row}')
        for row in partitions_cache:
            print(f'{row}')

    return i


def main():
    answer = get_answer()
    print(f"The Answer to Project Euler 078 is {answer}")

    # The Answer to Project Euler 078 is


if __name__ == "__main__":
    main()
