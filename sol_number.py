"""帝國火星暦の通算日."""

import math


class SolNumber(object):
    """帝國火星暦の通算日."""

    sol_number: float

    def __init__(self, sol_number: float) -> None:
        """Init."""
        if isinstance(sol_number, SolNumber):
            sol_number = sol_number.sol_number
        self.sol_number = sol_number

    def __eq__(self, other) -> bool:
        """Eq."""
        if not isinstance(other, SolNumber):
            return False
        return math.isclose(self.sol_number, other.sol_number, abs_tol=0.00001)

    @property
    def date(self) -> int:
        """年月日を表はす整數部分."""
        return math.floor(self.sol_number)

    @property
    def time(self) -> float:
        """日時を表はす小數部分."""
        return self.sol_number % 1
