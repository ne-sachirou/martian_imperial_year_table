"""Test ImperialDateTime."""

from imperial_calendar.ImperialDateTime import ImperialDateTime
import unittest


class TestImperialDateTime(unittest.TestCase):
    """Test ImperialDateTime."""

    def test_eq(self):
        """等値性."""
        self.assertEqual(ImperialDateTime(1, 2, 3, 4, 5, 6), ImperialDateTime(1, 2, 3, 4, 5, 6))
        self.assertNotEqual(ImperialDateTime(1, 2, 3, 4, 5, 6), ImperialDateTime(1, 2, 3, 4, 5, 7))