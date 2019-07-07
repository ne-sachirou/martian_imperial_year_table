"""Test GregorianDateTime."""
from imperial_calendar.GregorianDateTime import GregorianDateTime
import unittest


class TestGregorianDateTime(unittest.TestCase):
    """Test GregorianDateTime."""

    def test_from_utc_naive(self):
        """From UTC naive GregorianDateTime."""
        for (naive_grdt, grdt) in [
            (
                GregorianDateTime(1970, 1, 1, 0, 0, 0, None),
                GregorianDateTime(1970, 1, 1, 9, 0, 0, "+09:00"),
            ),
            (
                GregorianDateTime(1970, 1, 1, 0, 0, 0, None),
                GregorianDateTime(1970, 1, 1, 9, 0, 0, "Asia/Tokyo"),
            ),
            (
                GregorianDateTime(1970, 1, 1, 0, 0, 0, None),
                GregorianDateTime(1969, 12, 31, 15, 0, 0, "-09:00"),
            ),
        ]:
            with self.subTest(grdt=grdt):
                self.assertEqual(
                    grdt, GregorianDateTime.from_utc_naive(naive_grdt, grdt.timezone)
                )
        for (second, timezone) in [
            (second, timezone)
            for second in range(0, 60)
            for timezone in ["+00:00", "-00:00", "UTC"]
        ]:
            naive_grdt = GregorianDateTime(1970, 1, 1, 0, 0, second, None)
            grdt = GregorianDateTime(1970, 1, 1, 0, 0, second, timezone)
            with self.subTest(grdt=grdt):
                self.assertEqual(
                    grdt, GregorianDateTime.from_utc_naive(naive_grdt, timezone)
                )

    def test_to_utc_naive(self):
        """Convert to naive GregorianDateTime as UTC."""
        for (naive_grdt, grdt) in [
            (
                GregorianDateTime(1970, 1, 1, 0, 0, 0, None),
                GregorianDateTime(1970, 1, 1, 9, 0, 0, "+09:00"),
            ),
            (
                GregorianDateTime(1970, 1, 1, 0, 0, 0, None),
                GregorianDateTime(1970, 1, 1, 9, 0, 0, "Asia/Tokyo"),
            ),
            (
                GregorianDateTime(1970, 1, 1, 0, 0, 0, None),
                GregorianDateTime(1969, 12, 31, 15, 0, 0, "-09:00"),
            ),
        ]:
            with self.subTest(grdt=grdt):
                self.assertEqual(naive_grdt, grdt.to_utc_naive())
        for (second, timezone) in [
            (second, timezone)
            for second in range(0, 60)
            for timezone in ["+00:00", "-00:00", "UTC"]
        ]:
            naive_grdt = GregorianDateTime(1970, 1, 1, 0, 0, second, None)
            grdt = GregorianDateTime(1970, 1, 1, 0, 0, second, timezone)
            with self.subTest(grdt=grdt):
                self.assertEqual(naive_grdt, grdt.to_utc_naive())
