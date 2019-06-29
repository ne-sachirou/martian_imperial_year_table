"""Test conversions ImperialDateTime to ImperialSolNumber."""

from imperial_calendar import (ImperialDateTime, ImperialSolNumber)
from imperial_calendar.transform import imdt_to_imsn
import unittest


class Test_imdt_to_imsn(unittest.TestCase):
    """Test conversions ImperialDateTime to ImperialSolNumber."""

    def test_imdt_to_imsn(self):
        """Test conversions ImperialDateTime to ImperialSolNumber."""
        for (imdt, imsn) in [(ImperialDateTime(0, 1, 1, 0, 0, 0, 0.0), ImperialSolNumber(0.0)),
                             (ImperialDateTime(1000, 1, 1, 0, 0, 0, 0.0), ImperialSolNumber(668596.0)),
                             (ImperialDateTime(1, 1, 1, 6, 14, 25, 0.0), ImperialSolNumber(668.26002)),
                             (ImperialDateTime(1987, 6, 7, 12, 40, 30, 0.0), ImperialSolNumber(1328646.52813)),
                             (ImperialDateTime(3, 4, 5, 6, 7, 8, 0.0), ImperialSolNumber(2093.25496)),
                             (ImperialDateTime(-1, 24, 28, 0, 0, 0, 0.0), ImperialSolNumber(-1.0))]:
            self.assertEqual(imsn, imdt_to_imsn(imdt))
