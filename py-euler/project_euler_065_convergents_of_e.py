"""
    Convergents of e

    Problem 65

    Continued fraction of e:
    [2; 1, 2, 1, 1, 4, 1, 1, 6, 1, ..., 1, 2k, 1, ...]

    Find the sum of digits in the numerator of the 100th convergent of the continued fraction of e

"""
import math
from typing import List

debug = True


def investigate():
    e_cf = [3] + [6 for i in range(100)]
    n = 0
    d = 1

    e_cf = [2, 1, 2, 1, 1, 4, 1]
    depth = len(e_cf) - 1

    print(f'continued fraction {e_cf[:(depth+1)]}')
    for i in range(depth, -1, -1):
        n_new = int(d)
        d_new = int(e_cf[i] * d + n)
        c = math.gcd(n_new, d_new)
        n = int(n_new / c)
        d = int(d_new / c)

        print(f'e_cf[{i}]: {e_cf[i]}, convergent: {d}/{n} = {round(d/n, 8)}')

    return sum([int(c) for c in str(n)])


def get_convergent(cf: List[int], limit: int):
    n = 0
    d = 1
    for i in range(limit-1, -1, -1):
        n_new = int(d)
        d_new = int(cf[i] * d + n)
        c = math.gcd(n_new, d_new)
        n = int(n_new / c)
        d = int(d_new / c)
    return d, n


def get_answer():
    e_cf = [2] + [1 if i % 3 != 1 else int(2*(i+2)/3) for i in range(100)]
    n = 0
    d = 1
    if debug:
        print(f"continued fraction for e: {e_cf}")

    for i in range(1, 101):
        n, d = get_convergent(e_cf, i)
        if debug:
            print(f'#{i}: Using number {e_cf[i-1]}, convergent: {n}/{d} = {round(n/d, 8)}, sum of digits in numerator: '
                  f'{sum([int(c) for c in str(n)])}')

    # for i in range(99, -1, -1):
    #     n_new = int(d)
    #     d_new = int(e_cf[i] * d + n)
    #     c = math.gcd(n_new, d_new)
    #     n = int(n_new / c)
    #     d = int(d_new / c)
    #     if debug:
    #         print(f'e_cf[{i}]: {e_cf[i]}, convergent: {d}/{n} = {round(d/n, 8)}')

    return sum([int(c) for c in str(n)])


def main():
    # if debug:
    #     investigate()

    answer = get_answer()
    print(f"The Answer to Project Euler 065 is {answer}")

    # The Answer to Project Euler 065 is ___

    # This is troubling. The answer looks like it is 70.  I should not really look up the answer though.
    # I'll find the issue at some point. The Project Euler website can't be wrong can it?¿


if __name__ == "__main__":
    main()
