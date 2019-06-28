"""帝國火星暦の通算日."""
import math


class ImperialSolNumber(object):
    """帝國火星暦の通算日."""

    def __init__(self, imperial_sol_number: float) -> None:
        """Init."""
        self.imperial_sol_number: float = imperial_sol_number

    def __eq__(self, other) -> bool:
        """Eq."""
        if not isinstance(other, ImperialSolNumber):
            return False
        return math.isclose(
            self.imperial_sol_number, other.imperial_sol_number, abs_tol=0.00001
        )

    @property
    def date(self) -> int:
        """年月日を表はす整數部分."""
        return math.floor(self.imperial_sol_number)

    @property
    def time(self) -> float:
        """日時を表はす小數部分."""
        return self.imperial_sol_number % 1
