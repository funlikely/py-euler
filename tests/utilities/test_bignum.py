from unittest import TestCase

from utilities.bignum import *


class TestBigNum(TestCase):
    def test_add(self):
        a = BigNum('099518671430235219628894890102423325116913619626622')
        b = BigNum('073267460800591547471830798392868535206946944540724')
        bigsum = a.add(b)
        self.assertEqual('172786132230826767100725688495291860323860564167346', bigsum.value.lstrip('0'))
