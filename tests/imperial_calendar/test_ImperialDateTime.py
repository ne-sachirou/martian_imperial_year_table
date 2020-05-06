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

    def test_lt(self):
        """より小さい."""
        self.assertTrue(
            ImperialDateTime(1, 2, 3, 4, 5, 6, None)
            < ImperialDateTime(1, 2, 3, 4, 5, 7, None)
        )
        self.assertFalse(
            ImperialDateTime(1, 2, 3, 4, 5, 6, None)
            < ImperialDateTime(1, 2, 3, 4, 5, 6, None)
        )
        self.assertTrue(
            ImperialDateTime(1, 2, 3, 4, 5, 6, None)
            < ImperialDateTime(1, 2, 3, 4, 6, 6, None)
        )
        self.assertTrue(
            ImperialDateTime(1, 2, 3, 4, 5, 6, None)
            < ImperialDateTime(1, 2, 3, 5, 5, 6, None)
        )
        self.assertTrue(
            ImperialDateTime(1, 2, 3, 4, 5, 6, None)
            < ImperialDateTime(1, 2, 4, 4, 5, 6, None)
        )
        self.assertTrue(
            ImperialDateTime(1, 2, 3, 4, 5, 6, None)
            < ImperialDateTime(1, 3, 3, 4, 5, 6, None)
        )
        self.assertTrue(
            ImperialDateTime(1, 2, 3, 4, 5, 6, None)
            < ImperialDateTime(2, 2, 3, 4, 5, 6, None)
        )
        self.assertTrue(
            ImperialDateTime(1, 2, 3, 5, 5, 5, "+01:00")
            < ImperialDateTime(1, 2, 3, 3, 5, 6, "-01:00")
        )
        self.assertFalse(
            ImperialDateTime(1, 2, 3, 5, 5, 6, "+01:00")
            < ImperialDateTime(1, 2, 3, 3, 5, 6, "-01:00")
        )

    def test_from_standard_naive(self):
        """From standard timezone naive ImperialDateTime."""
        for (hour, minute) in [
            (hour, minute) for hour in range(0, 23) for minute in [0, 15, 30, 45]
        ]:
            timezone = "-{:0>2}:{:0>2}".format(hour, minute)
            with self.subTest(timezone=timezone):
                self.assertEqual(
                    ImperialDateTime(1398, 1, 1, 0, 0, 0, timezone),
                    ImperialDateTime.from_standard_naive(
                        ImperialDateTime(1398, 1, 1, hour, minute, 0, None), timezone
                    ),
                )
            timezone = "+{:0>2}:{:0>2}".format(hour, minute)
            with self.subTest(timezone=timezone):
                self.assertEqual(
                    ImperialDateTime(1398, 1, 1, hour, minute, 0, timezone),
                    ImperialDateTime.from_standard_naive(
                        ImperialDateTime(1398, 1, 1, 0, 0, 0, None), timezone
                    ),
                )

    def test_japanese_month_name(self):
        """日本語 (火星語) 月名."""
        self.assertEqual(
            "立春", ImperialDateTime(1425, 1, 1, 0, 0, 0, "+00:00").japanese_month_name
        )
        self.assertEqual(
            "大寒", ImperialDateTime(1425, 24, 1, 0, 0, 0, "+00:00").japanese_month_name
        )

    def test_next_month(self):
        """翌月."""
        imdt = ImperialDateTime(1425, 1, 3, 4, 5, 6, "+01:00")
        self.assertEqual(
            ImperialDateTime(1425, 2, 1, 0, 0, 0, "+01:00"), imdt.next_month(),
        )
        self.assertEqual(
            ImperialDateTime(1425, 2, 1, 0, 0, 0, "+01:00"), imdt,
        )
        imdt = ImperialDateTime(1425, 24, 5, 4, 3, 2, "+02:00")
        self.assertEqual(
            ImperialDateTime(1426, 1, 1, 0, 0, 0, "+02:00"), imdt.next_month()
        )
        self.assertEqual(ImperialDateTime(1426, 1, 1, 0, 0, 0, "+02:00"), imdt)

    def test_offset(self):
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
            with self.subTest(timezone=timezone):
                self.assertTrue(
                    math.isclose(
                        expected,
                        ImperialDateTime(0, 1, 1, 1, 1, 1, timezone).offset,
                        abs_tol=0.000005,
                    )
                )
        for timezone in ["+00"]:
            with self.subTest(timezone=timezone), self.assertRaises(Exception):
                ImperialDateTime(0, 1, 1, 1, 1, 1, timezone).offset

    def test_prev_month(self):
        """先月."""
        imdt = ImperialDateTime(1425, 2, 3, 4, 5, 6, "+01:00")
        self.assertEqual(
            ImperialDateTime(1425, 1, 1, 0, 0, 0, "+01:00"), imdt.prev_month()
        )
        self.assertEqual(ImperialDateTime(1425, 1, 1, 0, 0, 0, "+01:00"), imdt)
        imdt = ImperialDateTime(1426, 1, 5, 4, 3, 2, "+02:00")
        self.assertEqual(
            ImperialDateTime(1425, 24, 1, 0, 0, 0, "+02:00"), imdt.prev_month()
        )
        self.assertEqual(ImperialDateTime(1425, 24, 1, 0, 0, 0, "+02:00"), imdt)

    def test_to_standard_naive(self):
        """Convert to naive ImperialDateTime as standard timezone."""
        for (hour, minute) in [
            (hour, minute) for hour in range(0, 23) for minute in [0, 15, 30, 45]
        ]:
            timezone = "-{:0>2}:{:0>2}".format(hour, minute)
            with self.subTest(timezone=timezone):
                self.assertEqual(
                    ImperialDateTime(1398, 1, 1, hour, minute, 0, None),
                    ImperialDateTime(1398, 1, 1, 0, 0, 0, timezone).to_standard_naive(),
                )
            timezone = "+{:0>2}:{:0>2}".format(hour, minute)
            with self.subTest(timezone=timezone):
                self.assertEqual(
                    ImperialDateTime(1398, 1, 1, 0, 0, 0, None),
                    ImperialDateTime(
                        1398, 1, 1, hour, minute, 0, timezone
                    ).to_standard_naive(),
                )
