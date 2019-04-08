"""Test SolNumber."""

import math
from martian_calendar import SolNumber
import unittest


class TestSolNumber(unittest.TestCase):
    """Test SolNumber."""

    def test_eq(self):
        """等値性."""
        self.assertEqual(SolNumber(0.0), SolNumber(0.0))
        self.assertNotEqual(SolNumber(0.0), SolNumber(0.1))

    def test_date(self):
        """整數部分."""
        self.assertEqual(1, SolNumber(1.2).date)
        self.assertEqual(-2, SolNumber(-1.2).date)

    def test_time(self):
        """小數部分."""
        self.assertTrue(math.isclose(0.2, SolNumber(1.2).time))
        self.assertTrue(math.isclose(0.8, SolNumber(-1.2).time))
