# Divisors utilities
import math
from typing import List

from utilities.primes import PrimeProcessor


def get_divisors(n: int) -> List:
    if n < 2:
        return [1]
    pp = PrimeProcessor(n)
    prime_factor_list = pp.prime_factors(n)
    divisor_list = [1]
    for p in prime_factor_list:
        new_divisor_list = []
        for j in range(prime_factor_list[p] + 1):
            for k in range(len(divisor_list)):
                new_divisor_list.append(int(math.pow(p, j)) * divisor_list[k])
        divisor_list += new_divisor_list
    divisor_list = list(dict.fromkeys(divisor_list))
    divisor_list.sort()
    return divisor_list[:(len(divisor_list) - 1)]
