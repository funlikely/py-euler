from unittest import TestCase
from project_euler_036_double_base_palindromes import *


class Test(TestCase):
    def test_get_doubledromes(self):
        actual = sum(get_doubledromes())
        self.assertEqual(actual, 872187)

