from unittest import TestCase

import sys

sys.path.insert(0, '..\\..\\..\\py-euler\\101_200\\')
from project_euler_102_triangle_containment import *


class Test(TestCase):
    def test_triangle_contains_origin(self):
        triangle = ((-2, -2), (-2, 2), (2, 0))
        actual = triangle_contains_origin(triangle)
        self.assertEqual(actual, True)

    def test_triangle_does_not_contain_origin(self):
        triangle = ((-2, -2), (-2, 2), (-6, 0))
        actual = triangle_contains_origin(triangle)
        self.assertEqual(actual, False)

