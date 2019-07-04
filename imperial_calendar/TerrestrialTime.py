"""地球時 (テレストリアルタイム)."""
import math


class TerrestrialTime(object):
    """地球時 (テレストリアルタイム)."""

    def __init__(self, terrestrial_time: float) -> None:
        """Init."""
        self.terrestrial_time: float = terrestrial_time

    def __eq__(self, other) -> bool:
        """Eq."""
        if not isinstance(other, TerrestrialTime):
            return False
        return math.isclose(
            self.terrestrial_time, other.terrestrial_time, abs_tol=0.00001
        )
