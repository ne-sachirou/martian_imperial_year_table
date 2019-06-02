"""Test conversions ImperialSolNumber to ImperialDateTime."""

from imperial_calendar import (ImperialDateTime, ImperialSolNumber)
from imperial_calendar.transform import imsn_to_imdt
import unittest


class Test_imsn_to_imdt(unittest.TestCase):
    """Test conversions ImperialSolNumber to ImperialDateTime."""

    def test_imsn_to_imdt(self):
        """Test conversions ImperialSolNumber to ImperialDateTime."""
        for (imdt, imsn) in [(ImperialDateTime(1, 1, 1, 6, 14, 25, 0.0), ImperialSolNumber(668.26002)),
                             (ImperialDateTime(1987, 6, 7, 12, 40, 30, 0.0), ImperialSolNumber(1328642.52813)),
                             (ImperialDateTime(3, 4, 5, 6, 7, 8, 0.0), ImperialSolNumber(2093.25496)),
                             (ImperialDateTime(-1, 24, 28, 0, 0, 0, 0.0), ImperialSolNumber(-1.0))]:
            self.assertEqual(imdt, imsn_to_imdt(imsn, 0.0))
