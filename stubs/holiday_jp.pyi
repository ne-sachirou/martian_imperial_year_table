from datetime import date
import typing as t

class HolidayJp(object):
    is_holiday: bool
    def __init__(self, date: t.Union[str, date]): ...
