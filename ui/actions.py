"""UI actions."""
from imperial_calendar.GregorianDateTime import GregorianDateTime
from imperial_calendar.ImperialDateTime import ImperialDateTime
from imperial_calendar.ImperialSolNumber import ImperialSolNumber
from imperial_calendar.JulianDay import JulianDay
from imperial_calendar.MarsSolDate import MarsSolDate
from imperial_calendar.TerrestrialTime import TerrestrialTime
import typing as t

# __pragma__("skip")
document: t.Any = 0
encodeURIComponent: t.Any = 0
fetch: t.Any = 0
JSON: t.Any = 0
# __pragma__("noskip")


class Api(object):
    """Client of Web API."""

    async def get_datetimes(self, params: dict) -> dict:
        """Get datetimes."""
        response = await fetch(
            f"/api/datetimes?params={encodeURIComponent(params)}", {"method": "GET"}
        )
        if not response.ok:
            raise Exception(f"{response.status}: {response.text()}")
        return await response.json()


def change_grdt_timezone(state, event):
    """Change grdt_timezone."""
    ref = state["grdt_ref"]
    grdt_timezone = document.getElementById(ref + "timezone").value
    grdt = state["grdt"].copy()
    grdt.timezone = grdt_timezone
    return {"grdt_timezone": grdt_timezone, "grdt": grdt}


def change_imdt_timezone(state, event):
    """Change imdt_timezone."""
    ref = state["imdt_ref"]
    imdt_timezone = document.getElementById(ref + "timezone").value
    imdt = state["imdt"].copy()
    imdt.timezone = imdt_timezone
    return {"imdt_timezone": imdt_timezone, "imdt": imdt}


def draw_datetimes(state, datetimes):
    """Draw the result of GET /api/datetimes."""
    grdt = datetimes["grdt"]
    grdt = GregorianDateTime(
        grdt["year"],
        grdt["month"],
        grdt["day"],
        grdt["hour"],
        grdt["minute"],
        grdt["second"],
        state["grdt_timezone"],
    )
    juld = JulianDay(datetimes["juld"]["julian_day"])
    tert = TerrestrialTime(datetimes["tert"]["terrestrial_time"])
    mrsd = MarsSolDate(datetimes["mrsd"]["mars_sol_date"])
    imsn = ImperialSolNumber(datetimes["imsn"]["imperial_sol_number"])
    imdt = datetimes["imdt"]
    imdt = ImperialDateTime(
        imdt["year"],
        imdt["month"],
        imdt["day"],
        imdt["hour"],
        imdt["minute"],
        imdt["second"],
        state["imdt_timezone"],
    )
    return {
        "grdt": grdt,
        "juld": juld,
        "delta_t": datetimes["delta_t"],
        "tert": tert,
        "mrls": datetimes["mrls"],
        "mrsd": mrsd,
        "imsn": imsn,
        "imdt": imdt,
    }


async def sync_by_grdt(state, actions, event):
    """Sync by grdt."""
    if event:
        event.stopPropagation()
        event.preventDefault()
    ref = state["grdt_ref"]
    params = JSON.stringify(
        {
            "grdt_timezone": state["grdt_timezone"],
            "imdt_timezone": state["imdt_timezone"],
            "grdt": {
                "year": int(document.getElementById(ref + "year").value),
                "month": int(document.getElementById(ref + "month").value),
                "day": int(document.getElementById(ref + "day").value),
                "hour": int(document.getElementById(ref + "hour").value),
                "minute": int(document.getElementById(ref + "minute").value),
                "second": int(document.getElementById(ref + "second").value),
            },
        }
    )
    datetimes = await Api().get_datetimes(params)
    actions["draw_datetimes"](datetimes)


async def sync_by_juld(state, event):
    """Sync by juld."""
    event.stopPropagation()
    event.preventDefault()
    ref = state["juld_ref"]
    params = JSON.stringify(
        {
            "grdt_timezone": state["grdt_timezone"],
            "imdt_timezone": state["imdt_timezone"],
            "juld": {"julian_day": float(document.getElementById(ref).value)},
        }
    )
    datetimes = await Api().get_datetimes(params)
    actions["draw_datetimes"](datetimes)


async def sync_by_tert(state, event):
    """Sync by tert."""
    event.stopPropagation()
    event.preventDefault()
    ref = state["tert_ref"]
    params = JSON.stringify(
        {
            "grdt_timezone": state["grdt_timezone"],
            "imdt_timezone": state["imdt_timezone"],
            "tert": {"terrestrial_time": float(document.getElementById(ref).value)},
        }
    )
    datetimes = await Api().get_datetimes(params)
    actions["draw_datetimes"](datetimes)


async def sync_by_mrsd(state, event):
    """Sync by mrsd."""
    event.stopPropagation()
    event.preventDefault()
    ref = state["mrsd_ref"]
    params = JSON.stringify(
        {
            "grdt_timezone": state["grdt_timezone"],
            "imdt_timezone": state["imdt_timezone"],
            "mrsd": {"mars_sol_date": float(document.getElementById(ref).value)},
        }
    )
    datetimes = await Api().get_datetimes(params)
    actions["draw_datetimes"](datetimes)


async def sync_by_imsn(state, event):
    """Sync by imsn."""
    event.stopPropagation()
    event.preventDefault()
    ref = state["imsn_ref"]
    params = JSON.stringify(
        {
            "grdt_timezone": state["grdt_timezone"],
            "imdt_timezone": state["imdt_timezone"],
            "imsn": {"imperial_sol_number": float(document.getElementById(ref).value)},
        }
    )
    datetimes = await Api().get_datetimes(params)
    actions["draw_datetimes"](datetimes)


async def sync_by_imdt(state, event):
    """Sync by imdt."""
    event.stopPropagation()
    event.preventDefault()
    ref = state["imdt_ref"]
    params = JSON.stringify(
        {
            "grdt_timezone": state["grdt_timezone"],
            "imdt_timezone": state["imdt_timezone"],
            "imdt": {
                "year": int(document.getElementById(ref + "year").value),
                "month": int(document.getElementById(ref + "month").value),
                "day": int(document.getElementById(ref + "day").value),
                "hour": int(document.getElementById(ref + "hour").value),
                "minute": int(document.getElementById(ref + "minute").value),
                "second": int(document.getElementById(ref + "second").value),
            },
        }
    )
    datetimes = await Api().get_datetimes(params)
    actions["draw_datetimes"](datetimes)


def actions() -> t.Dict[str, t.Callable]:
    """Actions."""
    return {
        "change_grdt_timezone": lambda event: lambda state: change_grdt_timezone(
            state, event
        ),
        "change_imdt_timezone": lambda event: lambda state: change_imdt_timezone(
            state, event
        ),
        "draw_datetimes": lambda datetimes: lambda state: draw_datetimes(
            state, datetimes
        ),
        "sync_by_grdt": lambda event: lambda state, actions: sync_by_grdt(
            state, actions, event
        ),
        "sync_by_juld": lambda event: lambda state: sync_by_juld(state, event),
        "sync_by_tert": lambda event: lambda state: sync_by_tert(state, event),
        "sync_by_mrsd": lambda event: lambda state: sync_by_mrsd(state, event),
        "sync_by_imsn": lambda event: lambda state: sync_by_imsn(state, event),
        "sync_by_imdt": lambda event: lambda state: sync_by_imdt(state, event),
    }
