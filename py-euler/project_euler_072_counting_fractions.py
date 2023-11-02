"""
    Counting Fractions
    Problem 72

    Consider the fraction, $\dfrac n d$, where $n$ and $d$ are positive integers. If $n \lt d$ and $\operatorname{
    HCF}(n,d)=1$, it is called a reduced proper fraction.

    If we list the set of reduced proper fractions for
    $d \le 8$ in ascending order of size, we get: $$\frac 1 8, \frac 1 7, \frac 1 6, \frac 1 5, \frac 1 4, \frac 2 7,
    \frac 1 3, \frac 3 8, \frac 2 5, \frac 3 7, \frac 1 2, \frac 4 7, \frac 3 5, \frac 5 8, \frac 2 3, \frac 5 7,
    \frac 3 4, \frac 4 5, \frac 5 6, \frac 6 7, \frac 7 8$$

    It can be seen that there are 21 elements in this set.

    How many elements would be contained in the set of reduced proper fractions for d <= 10e6 ?

"""
import math
import time

from utilities.primes import PrimeProcessor
import utilities.divisors as div

debug = True

MAX_NUM = 1000
pp = PrimeProcessor()
primes = pp.get_primes_up_to(MAX_NUM)


def get_answer():
    max_d = 10**6+1
    n_d_sieve = [[True for i in range(max_d)] for j in range(max_d)]
    for i in range(2, max_d):
        for j in range(j, max_d, j):
            n_d_sieve = False
    return 1

def main():
    answer = get_answer()
    print(f"The Answer to Project Euler 072 is {answer}")

    # The Answer to Project Euler 072 is __


if __name__ == "__main__":
    main()
