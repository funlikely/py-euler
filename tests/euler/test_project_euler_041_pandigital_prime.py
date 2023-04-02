from unittest import TestCase
from project_euler_041_pandigital_prime import *


class Test(TestCase):
    def test_get_largest_4_digit_pandigital_prime(self):
        actual = get_largest_n_digit_pandigital_prime(4)
        self.assertEqual(4231, actual)

    def test_get_largest_5_digit_pandigital_prime(self):
        actual = get_largest_n_digit_pandigital_prime(5)
        self.assertEqual(4231, actual)
