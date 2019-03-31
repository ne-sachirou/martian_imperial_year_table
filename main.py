from martian_date_time import MartianDateTime
from martian_month import MartianMonth
from martian_year import MartianYear
import math
from sol_number import SolNumber


def sums(lst):
    "listを、先頭からの總和のlistに變換する"

    s = 0
    sums = []
    for item in lst:
        s += item
        sums.append(s)
    return sums


martian_year_to_sol_number_table = [0]
for year in range(0, 999):
    martian_year_to_sol_number_table.insert(year + 1, MartianYear(year).days())
martian_millennium_days = sum(martian_year_to_sol_number_table) + MartianYear(999).days()
martian_year_to_sol_number_table = sums(martian_year_to_sol_number_table)
martian_month_to_sol_number_table = [0]
for month in range(1, 24):
    martian_month_to_sol_number_table.insert(month, MartianMonth(month).days())
martian_month_to_sol_number_table = sums(martian_month_to_sol_number_table)


def sol_number_to_martian_date_time(sol_number):
    "帝國火星暦の通算日を日時に變換する"

    (millennium, days_in_millennium) = divmod(sol_number.date, martian_millennium_days)
    years_in_millennium = len(list(filter(lambda x: x <= days_in_millennium, martian_year_to_sol_number_table))) - 1
    days_before_new_years_day = martian_year_to_sol_number_table[years_in_millennium]
    days_in_year = days_in_millennium - days_before_new_years_day
    month = len(list(filter(lambda x: x <= days_in_year, martian_month_to_sol_number_table)))
    days_before_first_day_of_the_month = martian_month_to_sol_number_table[month - 1]
    return MartianDateTime(
        millennium * 1000 + years_in_millennium,
        month,
        days_in_year - days_before_first_day_of_the_month + 1,
        math.floor(sol_number.time * 24),
        math.floor((sol_number.time * 24 * 60) % 60),
        math.floor((sol_number.time * 24 * 60 * 60) % 60)
    )


def martian_date_time_to_sol_number(martian_date_time):
    "帝國火星暦の日時を通算日に變換する"

    days_of_millennium = martian_date_time.year // 1000 * martian_millennium_days
    days_in_millennium = martian_year_to_sol_number_table[martian_date_time.year % 1000]
    days_in_year = martian_month_to_sol_number_table[martian_date_time.month - 1]
    decimal_time = martian_date_time.hour / 24 + \
        martian_date_time.minute / (24 * 60) + \
        martian_date_time.second / (24 * 60 * 60)
    return SolNumber(
        days_of_millennium + \
        days_in_millennium + \
        days_in_year + \
        (martian_date_time.day - 1) + \
        decimal_time
    )
