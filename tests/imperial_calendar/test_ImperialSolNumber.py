"""Test ImperialSolNumber."""
import math
from imperial_calendar import ImperialSolNumber
import unittest


class TestImperialSolNumber(unittest.TestCase):
    """Test ImperialSolNumber."""

    def test_eq(self):
        """等値性."""
        self.assertEqual(ImperialSolNumber(0.0), ImperialSolNumber(0.0))
        self.assertNotEqual(ImperialSolNumber(0.0), ImperialSolNumber(0.1))

    def test_date(self):
        """整數部分."""
        self.assertEqual(1, ImperialSolNumber(1.2).date)
        self.assertEqual(-2, ImperialSolNumber(-1.2).date)

    def test_time(self):
        """小數部分."""
        self.assertTrue(math.isclose(0.2, ImperialSolNumber(1.2).time))
        self.assertTrue(math.isclose(0.8, ImperialSolNumber(-1.2).time))
