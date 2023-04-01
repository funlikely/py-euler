from unittest import TestCase
from project_euler_040_champernownes_constant import *

champer_ranges = [int(9 * x * math.pow(10, x - 1)) for x in range(1, 7)]
# [9, 180, 2700, 36000, 450000, 5400000]

champer_intervals = [sum(champer_ranges[:y]) for y in range(0, 7)]


# [0, 9, 189, 2889, 38889, 488889, 5888889]


class Test(TestCase):
    def test_get_champer_intervals_index_and_offset1(self):
        actual_index, actual_offset = get_champer_intervals_index_and_offset(1, champer_intervals)
        self.assertEqual(1, actual_offset)
        self.assertEqual(1, actual_index)

    def test_get_champer_intervals_index_and_offset10(self):
        actual_index, actual_offset = get_champer_intervals_index_and_offset(10, champer_intervals)
        self.assertEqual(1, actual_offset)
        self.assertEqual(2, actual_index)

    def test_get_champer_intervals_index_and_offset100(self):
        actual_index, actual_offset = get_champer_intervals_index_and_offset(100, champer_intervals)
        self.assertEqual(91, actual_offset)
        self.assertEqual(2, actual_index)

    def test_get_champer_intervals_index_and_offset1000(self):
        actual_index, actual_offset = get_champer_intervals_index_and_offset(1000, champer_intervals)
        self.assertEqual(811, actual_offset)
        self.assertEqual(3, actual_index)

    def test_get_champer_intervals_index_and_offset10000(self):
        actual_index, actual_offset = get_champer_intervals_index_and_offset(10000, champer_intervals)
        self.assertEqual(7111, actual_offset)
        self.assertEqual(4, actual_index)

    def test_get_champer_digit(self):
        actual = get_champer_digit(2, 91)
        self.assertEqual(5, actual)

        actual = get_champer_digit(3, 811)
        self.assertEqual(3, actual)

        actual = get_champer_digit(4, 7111)
        self.assertEqual(7, actual)

    def test_champernowne_challenge(self):
        actual = champernowne_challenge()
        self.assertEqual(210, actual)