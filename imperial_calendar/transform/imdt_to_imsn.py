"""帝國火星暦の日時を通算日に變換する."""
from imperial_calendar.ImperialDateTime import ImperialDateTime
from imperial_calendar.ImperialSolNumber import ImperialSolNumber
from imperial_calendar.internal.naive_imdt_to_imsn import naive_imdt_to_imsn
from imperial_calendar.internal.NaiveImperialDateTime import NaiveImperialDateTime


def imdt_to_imsn(imdt: ImperialDateTime) -> ImperialSolNumber:
    """帝國火星暦の日時を通算日に變換する."""
    naive_imdt = NaiveImperialDateTime(
        imdt.year, imdt.month, imdt.day, imdt.hour, imdt.minute, imdt.second
    )
    return naive_imdt_to_imsn(naive_imdt)
