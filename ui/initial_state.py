"""UI state."""
from imperial_calendar.GregorianDateTime import GregorianDateTime
from imperial_calendar.ImperialDateTime import ImperialDateTime
from imperial_calendar.ImperialSolNumber import ImperialSolNumber
from imperial_calendar.JulianDay import JulianDay
from imperial_calendar.MarsSolDate import MarsSolDate
from imperial_calendar.TerrestrialTime import TerrestrialTime
import typing as t

# __pragma__("skip")
Date: t.Any = 0
Math: t.Any = 0
# __pragma__("noskip")


def new_ref(prefix: str) -> str:
    """Create a React style reference."""
    return f"{prefix}.{Date.now().toString(36)}{Math.random().toString(36).substr(1)}"


def initial_state() -> dict:
    """Generate an initial state."""
    grdt_timezone = "+00:00"
    grdt = GregorianDateTime(1970, 1, 1, 0, 0, 0, grdt_timezone)
    juld = JulianDay(0, 0.0)
    tert = TerrestrialTime(0.0)
    mrsd = MarsSolDate(0.0)
    imsn = ImperialSolNumber(0, 0.0)
    imdt_timezone = "+00:00"
    imdt = ImperialDateTime(1, 1, 1, 0, 0, 0, imdt_timezone)
    return {
        "description": {"content": None, "ref": new_ref("description")},
        "global_navigation": {"is_active": False, "main_content": "transform"},
        "transform": {
            "grdt": grdt,
            "grdt_timezone": grdt_timezone,
            "juld": juld,
            "delta_t": 0.0,
            "tert": tert,
            "mrls": 0.0,
            "mrsd": mrsd,
            "imsn": imsn,
            "imdt": imdt,
            "imdt_timezone": imdt_timezone,
        },
    }
