import math
from sol_number import SolNumber
import unittest


class TestSolNumber(unittest.TestCase):
    def test_eq(self):
        self.assertEqual(SolNumber(0.0), SolNumber(0.0))
        self.assertNotEqual(SolNumber(0.0), SolNumber(0.1))

    def test_date(self):
        self.assertEqual(1, SolNumber(1.2).date)
        self.assertEqual(-2, SolNumber(-1.2).date)

    def test_time(self):
        self.assertTrue(math.isclose(0.2, SolNumber(1.2).time))
        self.assertTrue(math.isclose(0.8, SolNumber(-1.2).time))
