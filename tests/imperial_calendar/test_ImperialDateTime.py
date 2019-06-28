"""Test ImperialDateTime."""

from imperial_calendar.ImperialDateTime import ImperialDateTime
import math
import unittest


class TestImperialDateTime(unittest.TestCase):
    """Test ImperialDateTime."""

    def test_eq(self):
        """等値性."""
        self.assertEqual(
            ImperialDateTime(1, 2, 3, 4, 5, 6, "+00:00"),
            ImperialDateTime(1, 2, 3, 4, 5, 6, "+00:00"),
        )
        self.assertNotEqual(
            ImperialDateTime(1, 2, 3, 4, 5, 6, "+00:00"),
            ImperialDateTime(1, 2, 3, 4, 5, 7, "+00:00"),
        )

    def test_timezone(self):
        """Timezoneの文字列表現を内部表現にする."""
        for (expected, timezone) in [
            (0.0, "+00:00"),
            (0.0, "-00:00"),
            (0.25, "+00:15"),
            (1.0, "+01:00"),
            (23.75, "+23:45"),
            (-0.25, "-00:15"),
            (-23.75, "-23:45"),
        ]:
            self.assertTrue(
                math.isclose(
                    expected,
                    ImperialDateTime(0, 1, 1, 1, 1, 1, timezone).offset,
                    abs_tol=0.00001,
                )
            )
        for timezone in ["+00"]:
            with self.assertRaises(Exception):
                ImperialDateTime(0, 1, 1, 1, 1, 1, timezone).offset
