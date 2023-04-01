from unittest import TestCase
from project_euler_010_summation_of_primes import *


class Test(TestCase):
    def test_get_prime_sum(self):
        actual = get_prime_sum(10)
        self.assertEqual(17, actual)

    def test_get_prime_sum2(self):
        actual = get_prime_sum(20)
        self.assertEqual(77, actual)
