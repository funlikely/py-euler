from unittest import TestCase
from project_euler_039_integer_right_triangles import *


class Test(TestCase):
    def test_get_perimeter_that_maximizes_integer_right_triangles(self):
        actual = get_perimeter_that_maximizes_integer_right_triangles(111, False)
        self.assertEqual(60, actual)

    def test_get_triangles(self):
        actual = get_triangles(120)
        self.assertEqual([(30, 40, 50), (24, 45, 51), (20, 48, 52)], actual)
