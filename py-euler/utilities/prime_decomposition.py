"""
    Prime decomposition
    prime_decomposition of 1320 is 2^3 + 3^1 + 5^1 + 7^0 + 11^1, or [3, 1, 1, 0, 1]
"""
from utilities.primes import *


class PrimeDecomposition:

    def __init__(self, value):
        self.value = value
        self.pd = self.get_pd(value)
        self.pp = PrimeProcessor()

    def powerify(self, power):
        """raises a PrimeDecomposition to a power"""
        return [power * x for x in self.pd]

    def get_pd(self, value):
        return self.pp.prime_factors(value)[1]
