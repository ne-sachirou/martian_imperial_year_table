"""グレゴリオ暦の日時."""


class GregorianDateTime(object):
    """グレゴリオ暦の日時."""

    intercept = 1721088.5

    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int, timezone: float) -> None:
        """Init."""
        self.year: int = year
        self.month: int = month
        self.day: int = day
        self.hour: int = hour
        self.minute: int = minute
        self.second: int = second
        self.timezone: float = timezone

    def __eq__(self, other) -> bool:
        """Eq."""
        if not isinstance(other, GregorianDateTime):
            return False
        return self.__dict__ == other.__dict__
