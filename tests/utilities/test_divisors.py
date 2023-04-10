from unittest import TestCase

import utilities.divisors as d


class TestDivisors(TestCase):

    def test_get_divisors(self):
        actual_get_divisors = d.get_divisors(100)
        self.assertEqual(actual_get_divisors, [1, 2, 4, 5, 10, 20, 25, 50])

    def test_get_divisors2(self):
        actual_get_divisors = d.get_divisors(120)
        self.assertEqual(actual_get_divisors, [1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 24, 30, 40, 60])

    def test_get_divisors3(self):
        actual_get_divisors = d.get_divisors(50821)
        self.assertEqual(actual_get_divisors, [1])
