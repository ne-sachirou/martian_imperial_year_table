"""Mars Sol Date."""
import math


class MarsSolDate(object):
    """Mars Sol Date."""

    def __init__(self, mars_sol_date: float) -> None:
        """Init."""
        self.mars_sol_date: float = mars_sol_date

    def __eq__(self, other) -> bool:
        """Eq."""
        if not isinstance(other, MarsSolDate):
            return False
        return math.isclose(self.mars_sol_date, other.mars_sol_date, abs_tol=0.00001)

    def __repr__(self) -> str:
        """Representation."""
        return f"MarsSolDate({self.mars_sol_date})"
