"""火星帝國の祝日."""
from functools import total_ordering
from imperial_calendar.ImperialYearMonth import ImperialYearMonth
import typing as t


class Internal(object):
    """Internal data expression."""

    name: str

    def __init__(self, name: str):
        """Init."""
        self.name = name

    def __eq__(self, other: object) -> bool:
        """Eq."""
        return isinstance(other, Internal) and self.__dict__ == other.__dict__

    def __repr__(self) -> str:
        """Representation."""
        return f"Internal({self.name})"


HOLIDAYS: t.Dict[int, t.Dict[int, t.Dict[int, Internal]]] = {
    1425: {
        1: {
            1: Internal(name="四方節"),
            3: Internal(name="元始祭"),
            5: Internal(name="新年宴會"),
            15: Internal(name="元宵節"),
        },
        3: {15: Internal(name="春季皇靈祭")},
        6: {4: Internal(name="紀元節")},
        10: {3: Internal(name="夏至祭")},
        16: {24: Internal(name="神武天皇祭"), 25: Internal(name="秋季皇靈祭")},
        17: {19: Internal(name="天長節")},
        18: {20: Internal(name="地久節")},
        22: {1: Internal(name="冬至祭")},
    },
    1426: {
        1: {
            1: Internal(name="四方節"),
            3: Internal(name="元始祭"),
            5: Internal(name="新年宴會"),
            15: Internal(name="元宵節"),
        },
        3: {15: Internal(name="春季皇靈祭")},
        6: {4: Internal(name="紀元節")},
        10: {3: Internal(name="夏至祭")},
        16: {24: Internal(name="神武天皇祭"), 25: Internal(name="秋季皇靈祭")},
        17: {19: Internal(name="天長節")},
        18: {20: Internal(name="地久節")},
        22: {1: Internal(name="冬至祭")},
    },
}


@total_ordering
class HolidayMars(object):
    """火星帝國の祝日."""

    day: int
    internal: t.Optional[Internal]
    month: int
    year: int

    @classmethod
    def between(cls, lhs: "HolidayMars", rhs: "HolidayMars") -> t.List["HolidayMars"]:
        """List holidays on imdt in the period."""
        if lhs > rhs:
            return []
        holidays = []
        for year in range(
            max(lhs.year, min(HOLIDAYS.keys())),
            min(rhs.year, max(HOLIDAYS.keys())) + 1,
        ):
            for month in range(
                lhs.month if lhs.year == year else 1,
                (rhs.month if rhs.year == year else 24) + 1,
            ):
                if month in HOLIDAYS[year]:
                    for day in sorted(HOLIDAYS[year][month].keys()):
                        if day in range(
                            lhs.day if lhs.year == year and lhs.month == month else 1,
                            (
                                rhs.day
                                if rhs.year == year and rhs.month == month
                                else ImperialYearMonth(year, month).days()
                            )
                            + 1,
                        ):
                            holidays.append(cls(year, month, day))
        return holidays

    def __init__(self, year: int, month: int, day: int):
        """Init."""
        self.day = day
        self.internal = None
        self.month = month
        self.year = year
        if year in HOLIDAYS:
            hy = HOLIDAYS[year]
            if month in hy:
                hm = hy[month]
                if day in hm:
                    self.internal = hm[day]

    def __eq__(self, other: object) -> bool:
        """Eq."""
        return isinstance(other, HolidayMars) and self.__dict__ == other.__dict__

    def __lt__(self, other: "HolidayMars") -> bool:
        """Less than."""
        return self.year < other.year or (
            self.year == other.year
            and (
                self.month < other.month
                or (self.month == other.month and self.day < other.day)
            )
        )

    def __repr__(self) -> str:
        """Representation."""
        return f"HolidayMars({self.year}, {self.month}, {self.day}, internal={repr(self.internal)})"

    @property
    def is_holiday(self) -> bool:
        """Return the day is a holiday on imdt or not."""
        return self.internal is not None

    @property
    def name(self) -> t.Optional[str]:
        """Return the holiday name if the day is a holiday."""
        if self.internal is None:
            return None
        return self.internal.name
