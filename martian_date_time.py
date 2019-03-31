"""帝國火星暦の日時."""


class MartianDateTime(object):
    """帝國火星暦の日時."""

    year: int
    month: int
    day: int
    hour: int
    minute: int
    second: int

    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int) -> None:
        """Init."""
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second

    def __eq__(self, other) -> bool:
        """Eq."""
        if not isinstance(other, MartianDateTime):
            return False
        return self.__dict__ == other.__dict__
