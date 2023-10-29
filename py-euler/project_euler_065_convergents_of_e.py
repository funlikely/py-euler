"""
    Convergents of e

    Problem 65

    Continued fraction of e:
    [2; 1, 2, 1, 1, 4, 1, 1, 6, 1, ..., 1, 2k, 1, ...]

    Find the sum of digits in the numerator of the 100th convergent of the continued fraction of e

"""
import math


debug = True


def get_answer():
    e_cf = [2] + [1 if i % 3 != 1 else int(2*(i+2)/3) for i in range(100)]
    n = 1
    d = 1
    for i in range(99, -1, -1):
        print(f'e_cf[{i}]: {e_cf[i]}, convergent: {n}/{d}')
        n_new = int(e_cf[i] * d + e_cf[i])
        d_new = int(n)
        c = math.gcd(n_new, d_new)
        n = n_new / c
        d = d_new / d

    return 1


def investigate():
    return


def main():
    if debug:
        investigate()

    answer = get_answer()
    print(f"The Answer to Project Euler 065 is {answer}")

    # The Answer to Project Euler 065 is ___


if __name__ == "__main__":
    main()
