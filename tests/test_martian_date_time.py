"""Test MartianDateTime."""

from martian_date_time import MartianDateTime
import unittest


class TestMartianDateTime(unittest.TestCase):
    """Test MartianDateTime."""

    def test_eq(self):
        """等値性."""
        self.assertEqual(MartianDateTime(1, 2, 3, 4, 5, 6), MartianDateTime(1, 2, 3, 4, 5, 6))
        self.assertNotEqual(MartianDateTime(1, 2, 3, 4, 5, 6), MartianDateTime(1, 2, 3, 4, 5, 7))
