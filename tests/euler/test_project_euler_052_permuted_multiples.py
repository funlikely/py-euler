from unittest import TestCase
from project_euler_052_permuted_multiples import *


class Test(TestCase):
    def test_is_a_super_permuter(self):
        self.assertTrue(is_a_super_permuter(142857))

    def test_is_a_super_permuter2(self):
        self.assertFalse(is_a_super_permuter(123456))
