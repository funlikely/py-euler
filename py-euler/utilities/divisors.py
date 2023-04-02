# Divisors utilities
import math

from utilities.primes import prime_factors


def divisor_counter(a):
    if a < 0:
        return 0
    if a == 0 or a == 1:
        return 1
    count = 1
    for i in range(2, int(a / 2) + 1):
        if a % i == 0:
            count += 1
    return count + 1


def get_divisors(n):
    prime_factor_list = prime_factors(n)
    divisor_list = [1]
    for i in range(len(prime_factor_list[1])):
        new_divisor_list = []
        for j in range(prime_factor_list[1][i] + 1):
            for k in range(len(divisor_list)):
                if j > 0:
                    new_divisor_list.append(int(math.pow(prime_factor_list[0][i], j)) * divisor_list[k])
        divisor_list += new_divisor_list
    divisor_list = list(dict.fromkeys(divisor_list))
    divisor_list.sort()
    return divisor_list[:(len(divisor_list) - 1)]
