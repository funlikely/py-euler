import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# import utilities.primes as primes
# import utilities.prime_decomposition as prime_decomposition
# import utilities.divisors as divisors



# from .context import divisors  # utilities.divisors import divisor_counter, get_divisors

if __name__ == "__main__":
    suite = unittest.TestLoader().discover('.', pattern="test_*.py")
    unittest.TextTestRunner(verbosity=2).run(suite)
