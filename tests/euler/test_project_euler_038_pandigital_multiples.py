from unittest import TestCase

from project_euler_038_pandigital_multiples import PandigitalNumbers


class TestPandigitalNumbers(TestCase):

    def test_get_pandigital_numbers2(self):
        self.pandigital_numbers = PandigitalNumbers()
        p = self.pandigital_numbers
        assert max(p.get_pandigital_numbers2()) == "932718654"

    def test_get_pandigital_numbers3(self):
        p = PandigitalNumbers()
        assert max(p.get_pandigital_numbers3()) == "932718654"
