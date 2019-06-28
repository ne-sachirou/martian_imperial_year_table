"""グレゴリオ暦の日時."""
import typing as t

# __pragma__("skip")
from datetime import datetime, timedelta, timezone as tz_c, tzinfo
from pytz import timezone as tz, utc
import re

# __pragma__("noskip")


# __pragma__("skip")
def parse_timezone(timezone: str) -> tzinfo:
    """Parse timezone to offset."""
    match = re.match(
        r"^(?P<sign>[-+])(?P<hours>\d{1,2}):(?P<minutes>\d{1,2})$", timezone
    )
    if match:
        if match.group("sign") == "-":
            sign = -1
        else:
            sign = 1
        return tz_c(
            sign
            * timedelta(
                hours=int(match.group("hours")), minutes=int(match.group("minutes"))
            )
        )
    return tz(timezone)


# __pragma__("noskip")


class GregorianDateTime(object):
    """グレゴリオ暦の日時."""

    intercept = 1721088.5

    # __pragma__("skip")
    @classmethod
    def from_utc_naive(
        cls, grdt: "GregorianDateTime", timezone: str
    ) -> "GregorianDateTime":
        """From UTC naive GregorianDateTime."""
        if not (grdt.timezone is None):
            raise Exception(f"This is not naive: {grdt.__dict__}")
        dt = datetime(
            grdt.year,
            grdt.month,
            grdt.day,
            grdt.hour,
            grdt.minute,
            grdt.second,
            tzinfo=utc,
        )
        dt = dt.astimezone(parse_timezone(timezone))
        return cls(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, timezone)

    # __pragma__("noskip")

    def __init__(
        self,
        year: int,
        month: int,
        day: int,
        hour: int,
        minute: int,
        second: int,
        timezone: t.Optional[str],
    ) -> None:
        """Init."""
        self.year: int = year
        self.month: int = month
        self.day: int = day
        self.hour: int = hour
        self.minute: int = minute
        self.second: int = second
        self.timezone: t.Optional[str] = timezone

    def __eq__(self, other) -> bool:
        """Eq."""
        if not isinstance(other, GregorianDateTime):
            return False
        return self.__dict__ == other.__dict__

    def copy(self) -> "GregorianDateTime":
        """Shallow copy."""
        return self.__class__(
            self.year,
            self.month,
            self.day,
            self.hour,
            self.minute,
            self.second,
            self.timezone,
        )

    # __pragma__("skip")
    @property
    def offset(self) -> float:
        """Offset hours from UTC."""
        if self.timezone is None:
            raise Exception(f"This is naive: {self.__dict__}")
        return (
            parse_timezone(self.timezone).utcoffset(
                datetime(
                    self.year, self.month, self.day, self.hour, self.minute, self.second
                )
            )
            or timedelta(0)
        ).total_seconds() / (60.0 * 60.0)

    # __pragma__("noskip")

    # __pragma__("skip")
    def to_utc_naive(self) -> "GregorianDateTime":
        """Convert to naive GregorianDateTime as UTC."""
        if self.timezone is None:
            raise Exception(f"This is naive: {self.__dict__}")
        timezone = parse_timezone(self.timezone)
        dt: datetime
        try:
            dt = t.cast(t.Any, timezone).localize(
                datetime(
                    self.year, self.month, self.day, self.hour, self.minute, self.second
                )
            )
        except AttributeError:
            dt = datetime(
                self.year,
                self.month,
                self.day,
                self.hour,
                self.minute,
                self.second,
                tzinfo=timezone,
            )
        dt = dt.astimezone(utc)
        return GregorianDateTime(
            dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, None
        )

    # __pragma__("noskip")
