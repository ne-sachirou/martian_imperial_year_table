"""Test main."""

from imperial_calendar import (ImperialDateTime, imperial_date_time_to_sol_number, SolNumber,
                               sol_number_to_imperial_date_time)
import unittest


class TestSolNumberToImperialDateTime(unittest.TestCase):
    """Test conversions between SolNumner & ImperialDateTime."""

    def test_sol_number_to_imperial_date_time(self):
        """通算日と日時を相互に變換出來る."""
        for (imperial_date_time, sol_number) in [(ImperialDateTime(1, 1, 1, 6, 14, 25), SolNumber(668.26002)),
                                                 (ImperialDateTime(1987, 6, 7, 12, 40, 30), SolNumber(1328642.52813)),
                                                 (ImperialDateTime(3, 4, 5, 6, 7, 8), SolNumber(2093.25496)),
                                                 (ImperialDateTime(-1, 24, 28, 0, 0, 0), SolNumber(-1.0))]:
            self.assertEqual(imperial_date_time, sol_number_to_imperial_date_time(sol_number))
            self.assertEqual(sol_number, imperial_date_time_to_sol_number(imperial_date_time))
