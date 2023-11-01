"""
    Convergents of e

    Problem 65

    Continued fraction of e:
    [2; 1, 2, 1, 1, 4, 1, 1, 6, 1, ..., 1, 2k, 1, ...]

    Find the sum of digits in the numerator of the 100th convergent of the continued fraction of e

"""
import math
from typing import List

debug = False


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
    e_cf = [2] + [1 if i % 3 != 1 else int(2*(i+2)/3) for i in range(101)]
    n = 0
    d = 1
    if debug:
        print(f"continued fraction for e: {e_cf}")

    for i in range(1, 102):
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


def get_convergent_using_formula(cf, n):
    """
    Hardy number theory textbook Theorem 149

    If p(n) and q(n) are defined by
    p(0) = a(0), p(1) - a(1)*a(0) + 1, p(n) = a(n)*p(n-1) + p(n-2)
    q(0) = 1, q(1) = a(1), q(n) = a(n)*q(n-1)+q(n-2)
    then
    [a(0), a(1), ..., a(n)] = p(n)/q(n)

    :param cf:
    :param limit:
    :return:
    """
    p = [cf[0], cf[0] * cf[1] + 1]
    q = [1, cf[1]]
    for i in range(2, n):
        p.append(cf[i] * p[i-1] + p[i-2])
        q.append(cf[i] * q[i-1] + q[i-2])

    return p, q


def get_answer_a_different_way():
    e_cf = [2] + [1 if i % 3 != 1 else int(2*(i+2)/3) for i in range(101)]
    p, q = get_convergent_using_formula(e_cf, 101)

    if debug:
        for i in range(0, 101):
            print(f'#{i+1}: convergent: {p[i]}/{q[i]} = {round(p[i]/q[i], 8)}, sum of digits in numerator: '
                  f'{sum([int(c) for c in str(p[i])])}')

    return sum([int(c) for c in str(p[99])])


def main():
    # if debug:
    #     investigate()

    answer = get_answer_a_different_way()
    print(f"The Answer to Project Euler 065 is {answer}")

    # The Answer to Project Euler 065 is 272


if __name__ == "__main__":
    main()
