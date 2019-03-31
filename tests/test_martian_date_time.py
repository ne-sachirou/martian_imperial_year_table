from martian_date_time import MartianDateTime
import unittest


class TestMartianDateTime(unittest.TestCase):
    def test_eq(self):
        self.assertEqual(MartianDateTime(1, 2, 3, 4, 5, 6), MartianDateTime(1, 2, 3, 4, 5, 6))
        self.assertNotEqual(MartianDateTime(1, 2, 3, 4, 5, 6), MartianDateTime(1, 2, 3, 4, 5, 7))
