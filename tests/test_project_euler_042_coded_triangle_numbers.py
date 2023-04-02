from unittest import TestCase
from project_euler_042_coded_triangle_numbers import *


class Test(TestCase):
    def test_is_triangle1(self):
        actual = is_triangle('a')
        self.assertTrue(actual)

    def test_is_triangle2(self):
        actual = is_triangle('ab')
        self.assertTrue(actual)

    def test_is_triangle3(self):
        actual = is_triangle('HGFEDCBA')
        self.assertTrue(actual)

    def test_is_triangle4(self):
        actual = is_triangle('fd')
        self.assertTrue(actual)

    def test_is_triangle5(self):
        actual = is_triangle('b')
        self.assertFalse(actual)

    def test_is_triangle6(self):
        actual = is_triangle('CB')
        self.assertFalse(actual)


