from unittest import TestCase
from project_euler_035_circular_primes import *

class Test(TestCase):
    def test_get_circular_primes(self):
        actual = len(get_circular_primes())
        self.assertEqual(actual, 55)
