"""帝國火星暦の月."""


class MartianMonth(object):
    """帝國火星暦の月."""

    month: int

    def __init__(self, month: int) -> None:
        """Init."""
        self.month = month

    def days(self) -> int:
        """この月の日數."""
        if self.month % 6 == 0:
            return 27
        else:
            return 28
