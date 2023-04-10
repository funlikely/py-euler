from unittest import TestCase
from project_euler_012_highly_divisible_triangular_number import *


class Test(TestCase):
    def test_get_target_triangle_number(self):
        actual = get_target_triangle_number(False)
        self.assertEqual(actual, 76576500)
