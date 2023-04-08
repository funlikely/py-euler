from unittest import TestCase
from unittest.mock import MagicMock

import utilities.primes as p


class TestPrimes(TestCase):
    def test_prime_sieve(self):
        actual_prime_sieve = p.prime_sieve(3)
        self.assertEqual(actual_prime_sieve, [False, False, True, True, False, True])

    def test_get_primes(self):
        actual = p.get_primes(10)
        self.assertEqual(actual, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])

    def test_prime_factors(self):
        actual = p.prime_factors(15288)
        self.assertEqual(actual, [[2, 3, 5, 7, 11, 13], [3, 1, 0, 2, 0, 1]])

    def test_prime_factors(self):
        actual = p.prime_factors(5086121)
        self.assertTrue(5086121 in actual[0])  # 5086121 is prime

    def test_divisor_counter_fast(self):
        actual = p.divisor_counter_fast(15288)
        self.assertEqual(actual, 48)


class TestPrimeProcessor(TestCase):
    def test_get_prime_sieve_up_to_smaller_n_correctly_uses_cache(self):
        pp = p.PrimeProcessor(12)
        pp.old_get_prime_sieve_up_to = MagicMock()
        pp.get_prime_sieve_up_to(6)
        pp.old_get_prime_sieve_up_to.assert_not_called()

    def test_get_prime_sieve_up_to_greater_n_correctly_uses_cache(self):
        pp = p.PrimeProcessor(12)
        pp.generate_prime_sieve_up_to = MagicMock()
        pp.get_prime_sieve_up_to(18)
        pp.generate_prime_sieve_up_to.assert_called_with(18)

    def test_primes_up_to(self):
        pp = p.PrimeProcessor(50)
        actual = pp.primes_up_to(50)
        self.assertEqual(actual, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47])

    def test_get_prime_sieve_up_to(self):
        pp = p.PrimeProcessor()
        actual = pp.get_prime_sieve_up_to(14)
        self.assertEqual(actual, [False,
                                  False,
                                  True,
                                  True,
                                  False,
                                  True,
                                  False,
                                  True,
                                  False,
                                  False,
                                  False,
                                  True,
                                  False,
                                  True])
