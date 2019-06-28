"""帝國火星暦の通算日を日時に變換する."""
from imperial_calendar.ImperialSolNumber import ImperialSolNumber
from imperial_calendar.internal.consts import (
    imperial_millennium_days,
    imperial_year_to_imsn_table,
    imperial_month_to_imsn_table,
)
from imperial_calendar.internal.NaiveImperialDateTime import NaiveImperialDateTime
import math


def imsn_to_naive_imdt(imsn: ImperialSolNumber) -> NaiveImperialDateTime:
    """帝國火星暦の通算日を日時に變換する."""
    imsn = ImperialSolNumber(imsn.imperial_sol_number)
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
    return NaiveImperialDateTime(
        millennium * 1000 + years_in_millennium,
        month,
        days_in_year - days_before_first_day_of_the_month + 1,
        math.floor(imsn.time * 24),
        math.floor((imsn.time * 24 * 60) % 60),
        math.floor((imsn.time * 24 * 60 * 60) % 60),
    )
