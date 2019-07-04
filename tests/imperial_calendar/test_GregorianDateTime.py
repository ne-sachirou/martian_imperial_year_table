"""Test GregorianDateTime."""
from imperial_calendar.GregorianDateTime import GregorianDateTime
import unittest


class TestGregorianDateTime(unittest.TestCase):
    """Test GregorianDateTime."""

    def test_from_utc_naive(self):
        """From UTC naive GregorianDateTime."""
        self.assertEqual(
            GregorianDateTime(1970, 1, 1, 9, 0, 0, "+09:00"),
            GregorianDateTime.from_utc_naive(
                GregorianDateTime(1970, 1, 1, 0, 0, 0, None), "+09:00"
            ),
        )
        self.assertEqual(
            GregorianDateTime(1969, 12, 31, 15, 0, 0, "-09:00"),
            GregorianDateTime.from_utc_naive(
                GregorianDateTime(1970, 1, 1, 0, 0, 0, None), "-09:00"
            ),
        )

    def test_to_utc_naive(self):
        """Convert to naive GregorianDateTime as UTC."""
        self.assertEqual(
            GregorianDateTime(1970, 1, 1, 0, 0, 0, None),
            GregorianDateTime(1970, 1, 1, 9, 0, 0, "+09:00").to_utc_naive(),
        )
        self.assertEqual(
            GregorianDateTime(1970, 1, 1, 0, 0, 0, None),
            GregorianDateTime(1969, 12, 31, 15, 0, 0, "-09:00").to_utc_naive(),
        )
