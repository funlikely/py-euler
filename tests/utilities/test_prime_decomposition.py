from unittest import TestCase

from utilities.prime_decomposition import PrimeDecomposition


class TestPrimeDecomposition(TestCase):
    def test_powerify(self):
        pd = PrimeDecomposition(7560)
        actual_divisor_count = pd.powerify(4)
        self.assertEqual(actual_divisor_count, {2: 12, 3: 12, 5: 4, 7: 4})

    def test_powerify2(self):
        pd = PrimeDecomposition(11*17**3)
        actual_divisor_count = pd.powerify(5)
        self.assertEqual(actual_divisor_count, {11: 5, 17: 15})
