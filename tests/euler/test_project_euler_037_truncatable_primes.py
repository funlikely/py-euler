from unittest import TestCase
from project_euler_037_truncatable_primes import *
import utilities.primes as pr


class TestTruncatablePrimes(TestCase):
    def test_get_truncatable_primes_using_a_fold(self):
        actual = sum(get_truncatable_primes_using_a_fold())
        self.assertEqual(actual, 748317)

    def test_get_truncatable_primes_using_list_comprehension(self):
        actual = sum(get_truncatable_primes_using_list_comprehension())
        self.assertEqual(actual, 748317)

    def test_get_truncatable_primes(self):
        actual = sum(get_truncatable_primes())
        self.assertEqual(actual, 748317)