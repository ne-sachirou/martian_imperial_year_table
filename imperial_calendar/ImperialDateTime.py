"""帝國火星暦の日時."""
import re  # __:skip
import typing as t


# __pragma__("skip")
def parse_timezone(timezone: str) -> float:
    """Parse timezone to offset."""
    match = re.match(
        r"^(?P<sign>[-+])(?P<hours>\d{1,2}):(?P<minutes>\d{1,2})$", timezone
    )
    if match:
        if match.group("sign") == "-":
            sign = -1.0
        else:
            sign = 1.0
        return sign * (int(match.group("hours")) + (int(match.group("minutes")) / 60.0))
    raise Exception(f"Unknown timezone format: {timezone}")


# __pragma__("noskip")


class ImperialDateTime(object):
    """帝國火星暦の日時."""

    dummy = 42

    # __pragma__("skip")
    @classmethod
    def from_standard_naive(
        cls, imdt: "ImperialDateTime", timezone=str
    ) -> "ImperialDateTime":
        """From standard timezone naive ImperialDateTime."""
        from imperial_calendar.transform import imdt_to_imsn, imsn_to_imdt

        if not (imdt.timezone is None):
            raise Exception(f"This is not naive: {imdt.__dict__}")
        imsn = imdt_to_imsn(imdt)
        imsn.imperial_sol_number += parse_timezone(timezone) / 24.0
        imdt = imsn_to_imdt(imsn)
        imdt.timezone = timezone
        return imdt

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
        if not isinstance(other, ImperialDateTime):
            return False
        return self.__dict__ == other.__dict__

    def __repr__(self) -> str:
        """Representation."""
        return "ImperialDateTime({0},{1},{2},{3},{4},{5},{6})".format(
            self.year,
            self.month,
            self.day,
            self.hour,
            self.minute,
            self.second,
            repr(self.timezone),
        )

    def copy(self) -> "ImperialDateTime":
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
        """Parse timezone to offset."""
        if self.timezone is None:
            raise Exception(f"This is naive: {self.__dict__}")
        return parse_timezone(self.timezone)

    # __pragma__("noskip")

    # __pragma__("skip")
    def to_standard_naive(self) -> "ImperialDateTime":
        """Convert to naive ImperialDateTime as standard timezone."""
        from imperial_calendar.transform import imdt_to_imsn, imsn_to_imdt

        if self.timezone is None:
            raise Exception(f"This is naive: {self.__dict__}")
        imdt = self.copy()
        imdt.timezone = None
        imsn = imdt_to_imsn(imdt)
        imsn.imperial_sol_number -= self.offset / 24.0
        return imsn_to_imdt(imsn)

    # __pragma__("noskip")
