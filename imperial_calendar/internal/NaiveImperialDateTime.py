"""Timezoneを考慮しないImperialDateTime."""


class NaiveImperialDateTime(object):
    """Timezoneを考慮しないImperialDateTime."""

    def __init__(
        self, year: int, month: int, day: int, hour: int, minute: int, second: int
    ) -> None:
        """Init."""
        self.year: int = year
        self.month: int = month
        self.day: int = day
        self.hour: int = hour
        self.minute: int = minute
        self.second: int = second

    def __eq__(self, other) -> bool:
        """Eq."""
        if not isinstance(other, NaiveImperialDateTime):
            return False
        return self.__dict__ == other.__dict__
