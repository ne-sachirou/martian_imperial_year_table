"""グレゴリオ暦の日時をユリウス通日に變換する."""
from imperial_calendar.GregorianDateTime import GregorianDateTime
from imperial_calendar.JulianDay import JulianDay
import math


def grdt_to_juld(grdt: GregorianDateTime) -> JulianDay:
    """グレゴリオ暦の日時をユリウス通日に變換する."""
    if grdt.month in [1, 2]:
        tweaked_year = grdt.year - 1
        tweaked_month = grdt.month + 12
    else:
        tweaked_year = grdt.year
        tweaked_month = grdt.month
    return JulianDay(
        math.floor(tweaked_year * 365.25)
        + math.floor(tweaked_year / 400)
        - math.floor(tweaked_year / 100)
        + math.floor((tweaked_month - 2) * 30.59)
        + grdt.day
        + grdt.hour / 24
        + grdt.minute / (24 * 60)
        + grdt.second / (24 * 60 * 60)
        + grdt.intercept
    )
