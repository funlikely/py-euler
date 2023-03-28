from unittest import TestCase

from utilities.prime_decomposition import PrimeDecomposition


class TestPrimeDecomposition(TestCase):
    def test_powerify(self):
        pd = PrimeDecomposition(7560)
        actual_divisor_count = pd.powerify(4)
        self.assertEqual(actual_divisor_count, [12, 12, 4, 4])
