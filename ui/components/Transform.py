"""Transform component."""
from imperial_calendar.GregorianDateTime import GregorianDateTime
from imperial_calendar.ImperialDateTime import ImperialDateTime
from imperial_calendar.ImperialSolNumber import ImperialSolNumber
from imperial_calendar.JulianDay import JulianDay
from imperial_calendar.MarsSolDate import MarsSolDate
from imperial_calendar.TerrestrialTime import TerrestrialTime
from ui.Api import Api
import typing as t

React: t.Any = 0  # __:skip
ReactHookForm: t.Any = 0  # __:skip

__pragma__(  # noqa: F821
    "js",
    "{}",
    """
    window.process = {"env": {"NODE_ENV": "production"}}
    """,
)

INITIAL_DATETIME = {
    "grdt": GregorianDateTime(1970, 1, 1, 0, 0, 0, "+00:00"),
    "juld": JulianDay(2440587, 43200.0),
    "delta_t": 40.19294086136705,
    "tert": TerrestrialTime(2440587.500465196),
    "mrls": 295.3794638508962,
    "mrsd": MarsSolDate(34127.295516404454),
    "imsn": ImperialSolNumber(935321, 79532.61734358966),
    "imdt": ImperialDateTime(1398, 12, 22, 5, 23, 33, "+00:00"),
}


def set_grdt(form, grdt):
    """Set a grdt to the form."""
    form.setValue("grdt.year", grdt.year)
    form.setValue("grdt.month", grdt.month)
    form.setValue("grdt.day", grdt.day)
    form.setValue("grdt.hour", grdt.hour)
    form.setValue("grdt.minute", grdt.minute)
    form.setValue("grdt.second", grdt.second)
    form.setValue("grdt.timezone", grdt.timezone)


def set_juld(form, juld):
    """Set a juld to the form."""
    form.setValue("juld.julian_day", round(juld.julian_day, 5))


def set_delta_t(form, delta_t):
    """Set a delta_t to the form."""
    form.setValue("delta_t", round(delta_t, 5))


def set_tert(form, tert):
    """Set a tert to the form."""
    form.setValue("tert.terrestrial_time", round(tert.terrestrial_time, 5))


def set_mrls(form, mrls):
    """Set a mrls to the form."""
    form.setValue("mrls", round(mrls, 5))


def set_mrsd(form, mrsd):
    """Set a mrsd to the form."""
    form.setValue("mrsd.mars_sol_date", round(mrsd.mars_sol_date, 5))


def set_imsn(form, imsn):
    """Set a imsn to the form."""
    form.setValue("imsn.imperial_sol_number", round(imsn.imperial_sol_number, 5))


def set_imdt(form, imdt):
    """Set a imdt to the form."""
    form.setValue("imdt.year", imdt.year)
    form.setValue("imdt.month", imdt.month)
    form.setValue("imdt.day", imdt.day)
    form.setValue("imdt.hour", imdt.hour)
    form.setValue("imdt.minute", imdt.minute)
    form.setValue("imdt.second", imdt.second)
    form.setValue("imdt.timezone", imdt.timezone)


async def sync_by_grdt(form):
    """Sync a datetime by the grdt."""
    values = form.getValues()
    response = await Api().get_datetimes(
        {
            "grdt_timezone": values["grdt.timezone"],
            "imdt_timezone": values["imdt.timezone"],
            "grdt": {
                "year": int(values["grdt.year"]),
                "month": int(values["grdt.month"]),
                "day": int(values["grdt.day"]),
                "hour": int(values["grdt.hour"]),
                "minute": int(values["grdt.minute"]),
                "second": int(values["grdt.second"]),
            },
        },
    )
    set_juld(form, response.juld)
    set_delta_t(form, response.delta_t)
    set_tert(form, response.tert)
    set_mrls(form, response.mrls)
    set_mrsd(form, response.mrsd)
    set_imsn(form, response.imsn)
    set_imdt(form, response.imdt)


async def sync_by_juld(form):
    """Sync a datetime by the juld."""
    values = form.getValues()
    juld = JulianDay(float(values["juld.julian_day"]))
    response = await Api().get_datetimes(
        {
            "grdt_timezone": values["grdt.timezone"],
            "imdt_timezone": values["imdt.timezone"],
            "juld": {"day": juld.day, "second": juld.second},
        },
    )
    set_grdt(form, response.grdt)
    set_delta_t(form, response.delta_t)
    set_tert(form, response.tert)
    set_mrls(form, response.mrls)
    set_mrsd(form, response.mrsd)
    set_imsn(form, response.imsn)
    set_imdt(form, response.imdt)


async def sync_by_tert(form):
    """Sync a datetime by the tert."""
    values = form.getValues()
    response = await Api().get_datetimes(
        {
            "grdt_timezone": values["grdt.timezone"],
            "imdt_timezone": values["imdt.timezone"],
            "tert": {"terrestrial_time": float(values["tert.terrestrial_time"])},
        },
    )
    set_grdt(form, response.grdt)
    set_juld(form, response.juld)
    set_delta_t(form, response.delta_t)
    set_mrls(form, response.mrls)
    set_mrsd(form, response.mrsd)
    set_imsn(form, response.imsn)
    set_imdt(form, response.imdt)


async def sync_by_mrsd(form):
    """Sync a datetime by the mrsd."""
    values = form.getValues()
    response = await Api().get_datetimes(
        {
            "grdt_timezone": values["grdt.timezone"],
            "imdt_timezone": values["imdt.timezone"],
            "mrsd": {"mars_sol_date": float(values["mrsd.mars_sol_date"])},
        },
    )
    set_grdt(form, response.grdt)
    set_juld(form, response.juld)
    set_delta_t(form, response.delta_t)
    set_tert(form, response.tert)
    set_mrls(form, response.mrls)
    set_imsn(form, response.imsn)
    set_imdt(form, response.imdt)


async def sync_by_imsn(form):
    """Sync a datetime by the imsn."""
    values = form.getValues()
    imsn = ImperialSolNumber(float(values["imsn.imperial_sol_number"]))
    response = await Api().get_datetimes(
        {
            "grdt_timezone": values["grdt.timezone"],
            "imdt_timezone": values["imdt.timezone"],
            "imsn": {"day": imsn.day, "second": imsn.second},
        },
    )
    set_grdt(form, response.grdt)
    set_juld(form, response.juld)
    set_delta_t(form, response.delta_t)
    set_tert(form, response.tert)
    set_mrls(form, response.mrls)
    set_mrsd(form, response.mrsd)
    set_imdt(form, response.imdt)


async def sync_by_imdt(form):
    """Sync a datetime by the imdt."""
    values = form.getValues()
    response = await Api().get_datetimes(
        {
            "grdt_timezone": values["grdt.timezone"],
            "imdt_timezone": values["imdt.timezone"],
            "imdt": {
                "year": int(values["imdt.year"]),
                "month": int(values["imdt.month"]),
                "day": int(values["imdt.day"]),
                "hour": int(values["imdt.hour"]),
                "minute": int(values["imdt.minute"]),
                "second": int(values["imdt.second"]),
            },
        },
    )
    set_grdt(form, response.grdt)
    set_juld(form, response.juld)
    set_delta_t(form, response.delta_t)
    set_tert(form, response.tert)
    set_mrls(form, response.mrls)
    set_mrsd(form, response.mrsd)
    set_imsn(form, response.imsn)


def set_to_current(form):
    """Sync a datetime by the current grdt."""
    now = __new__(Date)  # noqa
    offset = now.getTimezoneOffset()
    if offset <= 0:
        sign = "+"
    else:
        sign = "-"
    grdt_timezone = "{0}{1}:{2}".format(
        sign,
        "0{}".format(abs(offset) // 60).substr(-2),
        "0{}".format(abs(offset) % 60).substr(-2),
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
    set_grdt(form, grdt)
    sync_by_grdt(form)


def SetToCurrent(props: dict):
    """Render a SetToCurrent component."""
    return React.createElement(
        "div",
        {},
        React.createElement(
            "button",
            {
                "className": "button is-dark",
                "onClick": lambda event: set_to_current(props.form),
            },
            "現在日時",
        ),
    )


def Grdt(props: dict):
    """Render a Grdt component."""
    return React.createElement(
        "div",
        {"className": "field is-grouped is-grouped-multiline"},
        React.createElement("label", {"className": "label"}, "Gregorian Date Time"),
        React.createElement(
            "input",
            {
                "className": "input",
                "defaultValue": INITIAL_DATETIME.grdt.year,
                "name": "grdt.year",
                "ref": props.form.register,
                "style": {"width": "6em"},
                "type": "number",
            },
        ),
        "-",
        React.createElement(
            "input",
            {
                "className": "input",
                "defaultValue": INITIAL_DATETIME.grdt.month,
                "max": 12,
                "min": 1,
                "name": "grdt.month",
                "ref": props.form.register,
                "style": {"width": "3.5em"},
                "type": "number",
            },
        ),
        "-",
        React.createElement(
            "input",
            {
                "className": "input",
                "defaultValue": INITIAL_DATETIME.grdt.day,
                "max": 31,
                "min": 1,
                "name": "grdt.day",
                "ref": props.form.register,
                "style": {"width": "3.5em"},
                "type": "number",
            },
        ),
        "T",
        React.createElement(
            "input",
            {
                "className": "input",
                "defaultValue": INITIAL_DATETIME.grdt.hour,
                "max": 23,
                "min": 0,
                "name": "grdt.hour",
                "ref": props.form.register,
                "style": {"width": "3.5em"},
                "type": "number",
            },
        ),
        ":",
        React.createElement(
            "input",
            {
                "className": "input",
                "defaultValue": INITIAL_DATETIME.grdt.minute,
                "max": 59,
                "min": 0,
                "name": "grdt.minute",
                "ref": props.form.register,
                "style": {"width": "3.5em"},
                "type": "number",
            },
        ),
        ":",
        React.createElement(
            "input",
            {
                "className": "input",
                "defaultValue": INITIAL_DATETIME.grdt.second,
                "max": 59,
                "min": 0,
                "name": "grdt.second",
                "ref": props.form.register,
                "style": {"width": "3.5em"},
                "type": "number",
            },
        ),
        React.createElement(
            "input",
            {
                "className": "input",
                "defaultValue": INITIAL_DATETIME.grdt.timezone,
                "name": "grdt.timezone",
                "ref": props.form.register,
                "style": {"width": "6em"},
                "type": "text",
            },
        ),
        React.createElement(
            "button",
            {
                "className": "button is-dark",
                "onClick": lambda event: sync_by_grdt(props.form),
            },
            "Sync",
        ),
    )


def Juld(props: dict):
    """Render a Juld component."""
    return React.createElement(
        "div",
        {"className": "field is-grouped"},
        React.createElement("label", {"className": "label"}, "Julian Day"),
        React.createElement(
            "input",
            {
                "className": "input",
                "defaultValue": round(INITIAL_DATETIME.juld.julian_day, 5),
                "name": "juld.julian_day",
                "ref": props.form.register,
                "step": 0.00001,
                "type": "number",
            },
        ),
        React.createElement(
            "button",
            {
                "className": "button is-dark",
                "onClick": lambda event: sync_by_juld(props.form),
            },
            "Sync",
        ),
    )


def DeltaT(props: dict):
    """Render a DeltaT component."""
    return React.createElement(
        "div",
        {"className": "field is-grouped"},
        React.createElement("div", {"className": "label"}, "⊿t"),
        React.createElement(
            "input",
            {
                "className": "input",
                "defaultValue": round(INITIAL_DATETIME.delta_t, 5),
                "disabled": True,
                "name": "delta_t",
                "ref": props.form.register,
                "step": 0.00001,
                "type": "number",
            },
        ),
    )


def Tert(props: dict):
    """Render a Tert component."""
    return React.createElement(
        "div",
        {"className": "field is-grouped"},
        React.createElement("div", {"className": "label"}, "Terrestrial Time"),
        React.createElement(
            "input",
            {
                "className": "input",
                "defaultValue": round(INITIAL_DATETIME.tert.terrestrial_time, 5),
                "name": "tert.terrestrial_time",
                "ref": props.form.register,
                "step": 0.00001,
                "type": "number",
            },
        ),
        React.createElement(
            "button",
            {
                "className": "button is-dark",
                "onClick": lambda event: sync_by_tert(props.form),
            },
            "Sync",
        ),
    )


def Mrls(props: dict):
    """Render a Mrls component."""
    return React.createElement(
        "div",
        {"className": "field is-grouped"},
        React.createElement(
            "div", {"className": "label"}, "Areocentric Solar Longitude (Mars Ls)"
        ),
        React.createElement(
            "input",
            {
                "className": "input",
                "defaultValue": round(INITIAL_DATETIME.mrls, 5),
                "disabled": True,
                "name": "mrls",
                "ref": props.form.register,
                "step": 0.00001,
                "type": "number",
            },
        ),
    )


def Mrsd(props: dict):
    """Render a Mrsd component."""
    return React.createElement(
        "div",
        {"className": "field is-grouped"},
        React.createElement("div", {"className": "label"}, "Mars Sol Date"),
        React.createElement(
            "input",
            {
                "className": "input",
                "defaultValue": round(INITIAL_DATETIME.mrsd.mars_sol_date, 5),
                "name": "mrsd.mars_sol_date",
                "ref": props.form.register,
                "step": 0.00001,
                "type": "number",
            },
        ),
        React.createElement(
            "button",
            {
                "className": "button is-dark",
                "onClick": lambda event: sync_by_mrsd(props.form),
            },
            "Sync",
        ),
    )


def Imsn(props: dict):
    """Render a Imsn component."""
    return React.createElement(
        "div",
        {"className": "field is-grouped"},
        React.createElement("div", {"className": "label"}, "Imperial Sol Number"),
        React.createElement(
            "input",
            {
                "className": "input",
                "defaultValue": round(INITIAL_DATETIME.imsn.imperial_sol_number, 5),
                "name": "imsn.imperial_sol_number",
                "ref": props.form.register,
                "step": 0.00001,
                "type": "number",
            },
        ),
        React.createElement(
            "button",
            {
                "className": "button is-dark",
                "onClick": lambda event: sync_by_imsn(props.form),
            },
            "Sync",
        ),
    )


def Imdt(props: dict):
    """Render a Imdt component."""
    return React.createElement(
        "div",
        {"className": "field is-grouped is-grouped-multiline"},
        React.createElement("label", {"className": "label"}, "Imperial Date Time"),
        React.createElement(
            "input",
            {
                "className": "input",
                "defaultValue": INITIAL_DATETIME.imdt.year,
                "name": "imdt.year",
                "ref": props.form.register,
                "style": {"width": "6em"},
                "type": "number",
            },
        ),
        "-",
        React.createElement(
            "input",
            {
                "className": "input",
                "defaultValue": INITIAL_DATETIME.imdt.month,
                "max": 24,
                "min": 1,
                "name": "imdt.month",
                "ref": props.form.register,
                "style": {"width": "3.5em"},
                "type": "number",
            },
        ),
        "-",
        React.createElement(
            "input",
            {
                "className": "input",
                "defaultValue": INITIAL_DATETIME.imdt.day,
                "max": 28,
                "min": 1,
                "name": "imdt.day",
                "ref": props.form.register,
                "style": {"width": "3.5em"},
                "type": "number",
            },
        ),
        "T",
        React.createElement(
            "input",
            {
                "className": "input",
                "defaultValue": INITIAL_DATETIME.imdt.hour,
                "max": 23,
                "min": 0,
                "name": "imdt.hour",
                "ref": props.form.register,
                "style": {"width": "3.5em"},
                "type": "number",
            },
        ),
        ":",
        React.createElement(
            "input",
            {
                "className": "input",
                "defaultValue": INITIAL_DATETIME.imdt.minute,
                "max": 59,
                "min": 0,
                "name": "imdt.minute",
                "ref": props.form.register,
                "style": {"width": "3.5em"},
                "type": "number",
            },
        ),
        ":",
        React.createElement(
            "input",
            {
                "className": "input",
                "defaultValue": INITIAL_DATETIME.imdt.second,
                "max": 59,
                "min": 0,
                "name": "imdt.second",
                "ref": props.form.register,
                "style": {"width": "3.5em"},
                "type": "number",
            },
        ),
        React.createElement(
            "input",
            {
                "className": "input",
                "defaultValue": INITIAL_DATETIME.imdt.timezone,
                "name": "imdt.timezone",
                "ref": props.form.register,
                "style": {"width": "6em"},
                "type": "text",
            },
        ),
        React.createElement(
            "button",
            {
                "className": "button is-dark",
                "onClick": lambda event: sync_by_imdt(props.form),
            },
            "Sync",
        ),
    )


def Transform(props: dict):
    """Render a Transform component."""
    form = ReactHookForm.useForm()
    React.useEffect(lambda: set_to_current(form), [])
    return React.createElement(
        "form",
        {"onSubmit": lambda event: event.preventDefault()},
        React.createElement(SetToCurrent, {"form": form}),
        React.createElement(Grdt, {"form": form}),
        React.createElement(Juld, {"form": form}),
        React.createElement(DeltaT, {"form": form}),
        React.createElement(Tert, {"form": form}),
        React.createElement(Mrls, {"form": form}),
        React.createElement(Mrsd, {"form": form}),
        React.createElement(Imsn, {"form": form}),
        React.createElement(Imdt, {"form": form}),
    )
