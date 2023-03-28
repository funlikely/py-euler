from unittest import TestCase

from .context import divisors  # utilities.divisors import divisor_counter, get_divisors


class Test(TestCase):
    def test_divisor_counter(self):
        actual_divisor_count = divisor_counter(100)
        self.assertEqual(actual_divisor_count, 9)

    def test_get_divisors(self):
        actual_get_divisors = get_divisors(100)
        self.assertEqual(actual_get_divisors, [1, 2, 4, 5, 10, 20, 25, 50])
