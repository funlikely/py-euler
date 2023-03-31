from unittest import TestCase
from project_euler_030_digit_fifth_powers import *


class Test(TestCase):
    def test_get_fifth_power_sums(self):
        actual = sum(get_fifth_power_sums())
        self.assertEqual(actual, 443839)
