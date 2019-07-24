"""UI transform actions."""
from imperial_calendar.GregorianDateTime import GregorianDateTime
from imperial_calendar.ImperialDateTime import ImperialDateTime
from imperial_calendar.ImperialSolNumber import ImperialSolNumber
from imperial_calendar.JulianDay import JulianDay
from imperial_calendar.MarsSolDate import MarsSolDate
from imperial_calendar.TerrestrialTime import TerrestrialTime
import typing as t

Date: t.Any = 0  # __:skip
document: t.Any = 0  # __:skip
setTimeout: t.Any = 0  # __:skip


class Api(object):
    """Client of Web API."""

    async def get_datetimes(self, params: dict) -> dict:
        """Get datetimes."""
        # __pragma__("skip")
        encodeURIComponent: t.Any = 0
        fetch: t.Any = 0
        JSON: t.Any = 0
        # __pragma__("noskip")
        response = await fetch(
            f"/api/datetimes?params={encodeURIComponent(JSON.stringify(params))}",
            {"method": "GET"},
        )
        if not response.ok:
            raise Exception(f"{response.status}: {response.text()}")
        return await response.json()


def change_grdt_attr(state, event, attr: str):
    """Change grdt attr."""
    value = int(event.target.value)
    grdt = state["grdt"].copy()
    setattr(grdt, attr, value)
    return {"grdt": grdt}


def change_grdt_timezone(state, event):
    """Change grdt_timezone."""
    grdt_timezone = event.target.value
    grdt = state["grdt"].copy()
    grdt.timezone = grdt_timezone
    return {"grdt_timezone": grdt_timezone, "grdt": grdt}


def change_juld(state, event):
    """Change juld."""
    return {"juld": state["juld"].__class__(float(event.target.value))}


def change_tert(state, event):
    """Change tert."""
    return {"tert": state["tert"].__class__(float(event.target.value))}


def change_mrsd(state, event):
    """Change mrsd."""
    return {"mrsd": state["mrsd"].__class__(float(event.target.value))}


def change_imsn(state, event):
    """Change imsn."""
    return {"imsn": state["imsn"].__class__(float(event.target.value))}


def change_imdt_attr(state, event, attr: str):
    """Change imdt attr."""
    value = int(event.target.value)
    imdt = state["imdt"].copy()
    setattr(imdt, attr, value)
    return {"imdt": imdt}


def change_imdt_timezone(state, event):
    """Change imdt_timezone."""
    imdt_timezone = event.target.value
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
    juld = datetimes["juld"]
    juld = JulianDay(juld["day"], juld["second"])
    tert = TerrestrialTime(datetimes["tert"]["terrestrial_time"])
    mrsd = MarsSolDate(datetimes["mrsd"]["mars_sol_date"])
    imsn = datetimes["imsn"]
    imsn = ImperialSolNumber(imsn["day"], imsn["second"])
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


def set_to_current(state, actions, event):
    """Set to current."""
    event.stopPropagation()
    event.preventDefault()
    now = __new__(Date)  # noqa
    offset = now.getTimezoneOffset()
    if offset <= 0:
        sign = "+"
    else:
        sign = "-"
    # grdt_timezone = "{0}{1:0>2}:{2:0>2}".format(
    #     sign, abs(offset) // 60, abs(offset) % 60
    # )
    grdt_timezone = "{0}{1}:{2}".format(
        sign, f"0{abs(offset) // 60}".substr(-2), f"0{abs(offset) % 60}".substr(-2)
    )
    grdt = GregorianDateTime(
        now.getFullYear(),
        now.getMonth() + 1,
        now.getDate(),
        now.getHours(),
        now.getMinutes(),
        now.getSeconds(),
        grdt_timezone,
    )
    setTimeout(lambda: actions["sync_by_grdt"](None), 0)
    return {"grdt": grdt, "grdt_timezone": grdt_timezone}


async def sync_by_grdt(state, actions, event):
    """Sync by grdt."""
    if event:
        event.stopPropagation()
        event.preventDefault()
    grdt = state["grdt"]
    params = {
        "grdt_timezone": state["grdt_timezone"],
        "imdt_timezone": state["imdt_timezone"],
        "grdt": {
            "year": grdt.year,
            "month": grdt.month,
            "day": grdt.day,
            "hour": grdt.hour,
            "minute": grdt.minute,
            "second": grdt.second,
        },
    }
    datetimes = await Api().get_datetimes(params)
    actions["draw_datetimes"](datetimes)


async def sync_by_juld(state, actions, event):
    """Sync by juld."""
    event.stopPropagation()
    event.preventDefault()
    juld = state["juld"]
    params = {
        "grdt_timezone": state["grdt_timezone"],
        "imdt_timezone": state["imdt_timezone"],
        "juld": {"day": juld.day, "second": juld.second},
    }
    datetimes = await Api().get_datetimes(params)
    actions["draw_datetimes"](datetimes)


async def sync_by_tert(state, actions, event):
    """Sync by tert."""
    event.stopPropagation()
    event.preventDefault()
    params = {
        "grdt_timezone": state["grdt_timezone"],
        "imdt_timezone": state["imdt_timezone"],
        "tert": {"terrestrial_time": state["tert"].terrestrial_time},
    }
    datetimes = await Api().get_datetimes(params)
    actions["draw_datetimes"](datetimes)


async def sync_by_mrsd(state, actions, event):
    """Sync by mrsd."""
    event.stopPropagation()
    event.preventDefault()
    params = {
        "grdt_timezone": state["grdt_timezone"],
        "imdt_timezone": state["imdt_timezone"],
        "mrsd": {"mars_sol_date": state["mrsd"].mars_sol_date},
    }
    datetimes = await Api().get_datetimes(params)
    actions["draw_datetimes"](datetimes)


async def sync_by_imsn(state, actions, event):
    """Sync by imsn."""
    event.stopPropagation()
    event.preventDefault()
    imsn = state["imsn"]
    params = {
        "grdt_timezone": state["grdt_timezone"],
        "imdt_timezone": state["imdt_timezone"],
        "imsn": {"day": imsn.day, "second": imsn.second},
    }
    datetimes = await Api().get_datetimes(params)
    actions["draw_datetimes"](datetimes)


async def sync_by_imdt(state, actions, event):
    """Sync by imdt."""
    event.stopPropagation()
    event.preventDefault()
    imdt = state["imdt"]
    params = {
        "grdt_timezone": state["grdt_timezone"],
        "imdt_timezone": state["imdt_timezone"],
        "imdt": {
            "year": imdt.year,
            "month": imdt.month,
            "day": imdt.day,
            "hour": imdt.hour,
            "minute": imdt.minute,
            "second": imdt.second,
        },
    }
    datetimes = await Api().get_datetimes(params)
    actions["draw_datetimes"](datetimes)


def transform_actions() -> t.Dict[str, t.Callable]:
    """UI transform actions."""
    return {
        "change_grdt_year": lambda event: lambda state: change_grdt_attr(
            state, event, "year"
        ),
        "change_grdt_month": lambda event: lambda state: change_grdt_attr(
            state, event, "month"
        ),
        "change_grdt_day": lambda event: lambda state: change_grdt_attr(
            state, event, "day"
        ),
        "change_grdt_hour": lambda event: lambda state: change_grdt_attr(
            state, event, "hour"
        ),
        "change_grdt_minute": lambda event: lambda state: change_grdt_attr(
            state, event, "minute"
        ),
        "change_grdt_second": lambda event: lambda state: change_grdt_attr(
            state, event, "second"
        ),
        "change_grdt_timezone": lambda event: lambda state: change_grdt_timezone(
            state, event
        ),
        "change_juld": lambda event: lambda state: change_juld(state, event),
        "change_tert": lambda event: lambda state: change_tert(state, event),
        "change_mrsd": lambda event: lambda state: change_mrsd(state, event),
        "change_imsn": lambda event: lambda state: change_imsn(state, event),
        "change_imdt_year": lambda event: lambda state: change_imdt_attr(
            state, event, "year"
        ),
        "change_imdt_month": lambda event: lambda state: change_imdt_attr(
            state, event, "month"
        ),
        "change_imdt_day": lambda event: lambda state: change_imdt_attr(
            state, event, "day"
        ),
        "change_imdt_hour": lambda event: lambda state: change_imdt_attr(
            state, event, "hour"
        ),
        "change_imdt_minute": lambda event: lambda state: change_imdt_attr(
            state, event, "minute"
        ),
        "change_imdt_second": lambda event: lambda state: change_imdt_attr(
            state, event, "second"
        ),
        "change_imdt_timezone": lambda event: lambda state: change_imdt_timezone(
            state, event
        ),
        "draw_datetimes": lambda datetimes: lambda state: draw_datetimes(
            state, datetimes
        ),
        "set_to_current": lambda event: lambda state, actions: set_to_current(
            state, actions, event
        ),
        "sync_by_grdt": lambda event: lambda state, actions: sync_by_grdt(
            state, actions, event
        ),
        "sync_by_juld": lambda event: lambda state, actions: sync_by_juld(
            state, actions, event
        ),
        "sync_by_tert": lambda event: lambda state, actions: sync_by_tert(
            state, actions, event
        ),
        "sync_by_mrsd": lambda event: lambda state, actions: sync_by_mrsd(
            state, actions, event
        ),
        "sync_by_imsn": lambda event: lambda state, actions: sync_by_imsn(
            state, actions, event
        ),
        "sync_by_imdt": lambda event: lambda state, actions: sync_by_imdt(
            state, actions, event
        ),
    }
