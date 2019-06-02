"""帝國火星暦の通算日を日時に變換する."""
from imperial_calendar.ImperialDateTime import ImperialDateTime
from imperial_calendar.ImperialSolNumber import ImperialSolNumber
from imperial_calendar.transform.consts import (
    imperial_millennium_days,
    imperial_year_to_imsn_table,
    imperial_month_to_imsn_table,
)
import math


def imsn_to_imdt(imsn: ImperialSolNumber, timezone: float) -> ImperialDateTime:
    """帝國火星暦の通算日を日時に變換する."""
    imsn = ImperialSolNumber(imsn.imperial_sol_number + timezone / 24)
    (millennium, days_in_millennium) = divmod(imsn.date, imperial_millennium_days)
    years_in_millennium = (
        len(
            list(filter(lambda x: x <= days_in_millennium, imperial_year_to_imsn_table))
        )
        - 1
    )
    days_before_new_years_day = imperial_year_to_imsn_table[years_in_millennium]
    days_in_year = days_in_millennium - days_before_new_years_day
    month = len(list(filter(lambda x: x <= days_in_year, imperial_month_to_imsn_table)))
    days_before_first_day_of_the_month = imperial_month_to_imsn_table[month - 1]
    return ImperialDateTime(
        millennium * 1000 + years_in_millennium,
        month,
        days_in_year - days_before_first_day_of_the_month + 1,
        math.floor(imsn.time * 24),
        math.floor((imsn.time * 24 * 60) % 60),
        math.floor((imsn.time * 24 * 60 * 60) % 60),
        timezone,
    )
