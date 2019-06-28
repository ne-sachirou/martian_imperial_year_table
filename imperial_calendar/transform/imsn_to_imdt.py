"""帝國火星暦の通算日を日時に變換する."""
from imperial_calendar.ImperialDateTime import ImperialDateTime
from imperial_calendar.ImperialSolNumber import ImperialSolNumber
from imperial_calendar.internal.imsn_to_naive_imdt import imsn_to_naive_imdt


def imsn_to_imdt(imsn: ImperialSolNumber) -> ImperialDateTime:
    """帝國火星暦の通算日を日時に變換する."""
    naive_imdt = imsn_to_naive_imdt(imsn)
    return ImperialDateTime(
        naive_imdt.year,
        naive_imdt.month,
        naive_imdt.day,
        naive_imdt.hour,
        naive_imdt.minute,
        naive_imdt.second,
        None,
    )
