from unittest import TestCase
from project_euler_051_prime_digit_replacements import *


class Test(TestCase):
    def test_get_least_highly_replaceable_prime(self):
        actual = get_least_highly_replaceable_prime(7)
        self.assertEquals(56003, actual)

    def test_get_least_highly_replaceable_prime2(self):
        actual = get_least_highly_replaceable_prime(8)
        self.assertEquals(121313, actual)
