"""帝國火星暦の日時を通算日に變換する."""
from imperial_calendar.ImperialDateTime import ImperialDateTime
from imperial_calendar.ImperialSolNumber import ImperialSolNumber
from imperial_calendar.transform.consts import (imperial_millennium_days, imperial_year_to_imsn_table,
                                                imperial_month_to_imsn_table)


def imdt_to_imsn(imdt: ImperialDateTime) -> ImperialSolNumber:
    """帝國火星暦の日時を通算日に變換する."""
    days_of_millennium = imdt.year // 1000 * imperial_millennium_days
    days_in_millennium = imperial_year_to_imsn_table[imdt.year % 1000]
    days_in_year = imperial_month_to_imsn_table[imdt.month - 1]
    decimal_time = imdt.hour / 24 + imdt.minute / (24 * 60) + imdt.second / (24 * 60 * 60)
    return ImperialSolNumber(days_of_millennium + days_in_millennium + days_in_year + (imdt.day - 1) + decimal_time - (imdt.timezone / 24))
