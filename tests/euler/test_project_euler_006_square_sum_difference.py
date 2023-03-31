from unittest import TestCase

from project_euler_006_square_sum_difference import *


class Test(TestCase):
    def test_get_square_sum_difference(self):
        actual = get_square_sum_difference()
        self.assertEqual(actual, 25164150)
