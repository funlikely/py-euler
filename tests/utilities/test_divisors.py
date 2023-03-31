from unittest import TestCase

import utilities.divisors as d


class TestDivisors(TestCase):
    def test_divisor_counter(self):
        actual_divisor_count = d.divisor_counter(100)
        self.assertEqual(actual_divisor_count, 9)

    def test_get_divisors(self):
        actual_get_divisors = d.get_divisors(100)
        self.assertEqual(actual_get_divisors, [1, 2, 4, 5, 10, 20, 25, 50])
