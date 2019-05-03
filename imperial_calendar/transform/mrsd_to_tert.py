"""MSDから地球時を算出する."""
from imperial_calendar.MarsSolDate import MarsSolDate
from imperial_calendar.TerrestrialTime import TerrestrialTime


def mrsd_to_tert(mrsd: MarsSolDate) -> TerrestrialTime:
    """MSDから地球時を算出する."""
    return TerrestrialTime(1.027491252 * (mrsd.mars_sol_date - 44796 + 0.00096) + 2451545 + 4.5)
