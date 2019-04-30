"""imperial_calendar."""

from imperial_calendar.ImperialDateTime import ImperialDateTime
from imperial_calendar.ImperialMonth import ImperialMonth
from imperial_calendar.ImperialYear import ImperialYear
from imperial_calendar.SolNumber import SolNumber
import math


def sums(lst):
    """listを、先頭からの總和のlistに變換する."""
    s = 0
    sums = []
    for item in lst:
        s += item
        sums.append(s)
    return sums


imperial_year_to_sol_number_table = [0]
for year in range(0, 999):
    imperial_year_to_sol_number_table.insert(year + 1, ImperialYear(year).days())
imperial_millennium_days = sum(imperial_year_to_sol_number_table) + ImperialYear(999).days()  # type: int
imperial_year_to_sol_number_table = sums(imperial_year_to_sol_number_table)
imperial_month_to_sol_number_table = [0]
for month in range(1, 24):
    imperial_month_to_sol_number_table.insert(month, ImperialMonth(month).days())
imperial_month_to_sol_number_table = sums(imperial_month_to_sol_number_table)


def sol_number_to_imperial_date_time(sol_number: SolNumber) -> ImperialDateTime:
    """帝國火星暦の通算日を日時に變換する."""
    (millennium, days_in_millennium) = divmod(sol_number.date, imperial_millennium_days)
    years_in_millennium = len(list(filter(lambda x: x <= days_in_millennium, imperial_year_to_sol_number_table))) - 1
    days_before_new_years_day = imperial_year_to_sol_number_table[years_in_millennium]
    days_in_year = days_in_millennium - days_before_new_years_day
    month = len(list(filter(lambda x: x <= days_in_year, imperial_month_to_sol_number_table)))
    days_before_first_day_of_the_month = imperial_month_to_sol_number_table[month - 1]
    return ImperialDateTime(millennium * 1000 + years_in_millennium, month,
                            days_in_year - days_before_first_day_of_the_month + 1, math.floor(sol_number.time * 24),
                            math.floor((sol_number.time * 24 * 60) % 60),
                            math.floor((sol_number.time * 24 * 60 * 60) % 60))


def imperial_date_time_to_sol_number(imperial_date_time: ImperialDateTime) -> SolNumber:
    """帝國火星暦の日時を通算日に變換する."""
    days_of_millennium = imperial_date_time.year // 1000 * imperial_millennium_days
    days_in_millennium = imperial_year_to_sol_number_table[imperial_date_time.year % 1000]
    days_in_year = imperial_month_to_sol_number_table[imperial_date_time.month - 1]
    decimal_time = imperial_date_time.hour / 24 + \
        imperial_date_time.minute / (24 * 60) + \
        imperial_date_time.second / (24 * 60 * 60)
    return SolNumber(days_of_millennium + days_in_millennium + days_in_year + (imperial_date_time.day - 1) +
                     decimal_time)


__all__ = [
    "ImperialDateTime", "ImperialMonth", "ImperialYear", "imperial_date_time_to_sol_number", "SolNumber",
    "sol_number_to_imperial_date_time"
]
