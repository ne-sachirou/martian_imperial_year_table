"""UI state."""
from imperial_calendar.GregorianDateTime import GregorianDateTime
from imperial_calendar.ImperialDateTime import ImperialDateTime
from imperial_calendar.ImperialSolNumber import ImperialSolNumber
from imperial_calendar.JulianDay import JulianDay
from imperial_calendar.MarsSolDate import MarsSolDate
from imperial_calendar.TerrestrialTime import TerrestrialTime

Date = Math = 0  # __:skip


def new_ref(prefix: str) -> str:
    """Create a React style reference."""
    # fmt: off
    ref = f"{prefix}.{Date.now().toString(36)}{Math.random().toString(36).substr(1)}"  # type: ignore
    # fmt: on
    return ref


def initial_state() -> dict:
    """Generate an initial state."""
    grdt_timezone = "+00:00"
    grdt = GregorianDateTime(1970, 1, 1, 0, 0, 0, grdt_timezone)
    grdt_ref = new_ref("grdt")
    juld = JulianDay(0.0)
    juld_ref = new_ref("juld")
    tert = TerrestrialTime(0.0)
    tert_ref = new_ref("tert")
    mrsd = MarsSolDate(0.0)
    mrsd_ref = new_ref("mrsd")
    imsn = ImperialSolNumber(0.0)
    imsn_ref = new_ref("imsn")
    imdt_timezone = "+00:00"
    imdt = ImperialDateTime(0, 0, 0, 0, 0, 0, imdt_timezone)
    imdt_ref = new_ref("imdt")
    return {
        "description": {"content": None, "ref": new_ref("description")},
        "global_navigation": {"is_active": False, "main_content": "transform"},
        "transform": {
            "grdt": grdt,
            "grdt_ref": grdt_ref,
            "grdt_timezone": grdt_timezone,
            "juld": juld,
            "juld_ref": juld_ref,
            "delta_t": 0.0,
            "tert": tert,
            "tert_ref": tert_ref,
            "mrls": 0.0,
            "mrsd": mrsd,
            "mrsd_ref": mrsd_ref,
            "imsn": imsn,
            "imsn_ref": imsn_ref,
            "imdt": imdt,
            "imdt_ref": imdt_ref,
            "imdt_timezone": imdt_timezone,
        },
    }
