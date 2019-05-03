"""Imperial Calendar (帝國火星暦)."""
from imperial_calendar.GregorianDateTime import GregorianDateTime
from imperial_calendar.ImperialDateTime import ImperialDateTime
from imperial_calendar.ImperialMonth import ImperialMonth
from imperial_calendar.ImperialYear import ImperialYear
from imperial_calendar.ImperialSolNumber import ImperialSolNumber
from imperial_calendar.TerrestrialTime import TerrestrialTime


def gregorian_date_time_to_terrestrial_time(grdt: GregorianDateTime) -> TerrestrialTime:
    """グレゴリオ暦の日時を地球時に變換する."""
    from imperial_calendar.transform.grdt_to_juld import grdt_to_juld
    from imperial_calendar.transform.juld_to_tert import juld_to_tert
    return juld_to_tert(grdt_to_juld(grdt))


def sol_number_to_imperial_date_time(imsn: ImperialSolNumber) -> ImperialDateTime:
    """帝國火星暦の通算日を日時に變換する."""
    from imperial_calendar.transform.imsn_to_imdt import imsn_to_imdt
    return imsn_to_imdt(imsn, 0.0)


def imperial_date_time_to_sol_number(imdt: ImperialDateTime) -> ImperialSolNumber:
    """帝國火星暦の日時を通算日に變換する."""
    from imperial_calendar.transform.imdt_to_imsn import imdt_to_imsn
    return imdt_to_imsn(imdt)


__all__ = [
    "ImperialDateTime", "ImperialMonth", "ImperialYear", "imperial_date_time_to_sol_number", "ImperialSolNumber",
    "sol_number_to_imperial_date_time"
]
