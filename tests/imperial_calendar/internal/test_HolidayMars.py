"""Test HolidayMars."""
from imperial_calendar.internal.HolidayMars import HolidayMars
import unittest


class TestHolidayMars(unittest.TestCase):
    """Test HolidayMars."""

    def test_between(self):
        """該当期間中の祝日一覧."""
        for expected, start, end in [
            [
                [
                    HolidayMars(1425, 1, 1),
                    HolidayMars(1425, 1, 2),
                    HolidayMars(1425, 1, 3),
                    HolidayMars(1425, 1, 15),
                ],
                HolidayMars(1425, 1, 1),
                HolidayMars(1425, 1, 15),
            ],
            [
                [
                    HolidayMars(1425, 1, 2),
                    HolidayMars(1425, 1, 3),
                    HolidayMars(1425, 1, 15),
                ],
                HolidayMars(1425, 1, 2),
                HolidayMars(1425, 1, 15),
            ],
            [
                [
                    HolidayMars(1425, 1, 1),
                    HolidayMars(1425, 1, 2),
                    HolidayMars(1425, 1, 3),
                ],
                HolidayMars(1425, 1, 1),
                HolidayMars(1425, 1, 14),
            ],
            [
                [
                    HolidayMars(1425, 1, 15),
                    HolidayMars(1425, 1, 16),
                    HolidayMars(1425, 3, 15),
                ],
                HolidayMars(1425, 1, 15),
                HolidayMars(1425, 3, 15),
            ],
            [
                [
                    HolidayMars(1425, 22, 1),
                    HolidayMars(1425, 22, 2),
                    HolidayMars(1426, 1, 1),
                ],
                HolidayMars(1425, 22, 1),
                HolidayMars(1426, 1, 1),
            ],
        ]:
            with self.subTest(start=start, end=end):
                self.assertEqual(expected, HolidayMars.between(start, end))

    def test_is_holiday(self):
        """その日が祝日であるか否か."""
        self.assertTrue(HolidayMars(1425, 1, 1).is_holiday)
        self.assertFalse(HolidayMars(1425, 1, 4).is_holiday)

    def test_lt(self):
        """より小さい."""
        lhs, rhs = HolidayMars(2, 2, 2), HolidayMars(2, 2, 2)
        with self.subTest(lhs=lhs, rhs=rhs):
            self.assertFalse(lhs < rhs)
        for lhs, rhs in [
            [HolidayMars(1, 2, 2), HolidayMars(2, 2, 2)],
            [HolidayMars(2, 1, 2), HolidayMars(2, 2, 2)],
            [HolidayMars(2, 2, 1), HolidayMars(2, 2, 2)],
        ]:
            with self.subTest(lhs=lhs, rhs=rhs):
                self.assertTrue(lhs < rhs)
        for lhs, rhs in [
            [HolidayMars(2, 1, 2), HolidayMars(1, 2, 2)],
            [HolidayMars(2, 2, 1), HolidayMars(2, 1, 2)],
        ]:
            with self.subTest(lhs=lhs, rhs=rhs):
                self.assertFalse(lhs < rhs)
