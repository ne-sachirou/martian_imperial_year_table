"""Calendar component."""
from imperial_calendar.GregorianDateTime import GregorianDateTime
from imperial_calendar.ImperialDateTime import ImperialDateTime
from ui.Api import Api
from ui.utils import current_grdt
import typing as t

__pragma__(  # noqa: F821
    "js",
    "{}",
    """
    const React = require("react");
    const ReactHookForm = require("react-hook-form");
    window.process = {"env": {"NODE_ENV": "production"}}
    """,
)

document: t.Any = 0  # __:skip
encodeURIComponent: t.Any = 0  # __:skip
js_undefined: t.Any = 0  # __:skip
JSON: t.Any = 0  # __:skip
React: t.Any = 0  # __:skip
ReactHookForm: t.Any = 0  # __:skip

INITIAL_DATETIME = {
    "grdt": GregorianDateTime(1970, 1, 1, 0, 0, 0, "+00:00"),
    "imdt": ImperialDateTime(1398, 23, 12, 22, 5, 33, "+00:00"),
}


async def draw(form, ref) -> None:
    """Draw the calendar SVG."""
    grdt = current_grdt()
    values = form.getValues()
    params = {
        "grdt_timezone": grdt.timezone,
        "imdt": {"year": int(values["imdt.year"]), "month": int(values["imdt.month"])},
    }
    svg = await Api().get_calendar_svg(params)
    html = '<a href="/api/calendar.svg?params={}">{}</a>'.format(
        encodeURIComponent(JSON.stringify(params)), svg,
    )
    ref.current.innerHTML = html


async def set_to_current(form, ref) -> None:
    """Draw a calendar at now."""
    grdt = current_grdt()
    form.setValue("grdt.timezone", grdt.timezone)
    response = await Api().get_datetimes(
        {
            "grdt_timezone": grdt.timezone,
            "imdt_timezone": "+00:00",
            "grdt": {
                "year": grdt.year,
                "month": grdt.month,
                "day": grdt.day,
                "hour": grdt.hour,
                "minute": grdt.minute,
                "second": grdt.second,
            },
        },
    )
    form.setValue("imdt.year", response.imdt.year)
    form.setValue("imdt.month", response.imdt.month)
    await draw(form, ref)


async def turn_to_next(form, ref) -> None:
    """Turn the calendar to the next month."""
    values = form.getValues()
    imdt = ImperialDateTime(
        int(values["imdt.year"]), int(values["imdt.month"]), 1, 0, 0, 0, "+00:00"
    ).next_month()
    form.setValue("imdt.year", imdt.year)
    form.setValue("imdt.month", imdt.month)
    await draw(form, ref)


async def turn_to_previous(form, ref) -> None:
    """Turn the calendar to the previous month."""
    values = form.getValues()
    imdt = ImperialDateTime(
        int(values["imdt.year"]), int(values["imdt.month"]), 1, 0, 0, 0, "+00:00"
    ).prev_month()
    form.setValue("imdt.year", imdt.year)
    form.setValue("imdt.month", imdt.month)
    await draw(form, ref)


def Calendar(props: dict):
    """Render a Calendar component."""
    form = ReactHookForm.useForm()
    ref = React.useRef()
    React.useEffect(lambda: set_to_current(form, ref) and js_undefined, [form, ref])
    return React.createElement(
        "div",
        {"onSubmit": lambda event: event.preventDefault()},
        React.createElement(
            "form",
            {},
            React.createElement(
                "div",
                {"className": "field is-grouped"},
                React.createElement(
                    "label", {"className": "label"}, "Gregorian Date Time"
                ),
                React.createElement(
                    "input",
                    {
                        "className": "input",
                        "defaultValue": INITIAL_DATETIME.grdt.timezone,
                        "disabled": True,
                        "name": "grdt.timezone",
                        "ref": form.register,
                        "style": {"width": "6em"},
                        "type": "text",
                    },
                ),
            ),
            React.createElement(
                "div",
                {"className": "field is-grouped"},
                React.createElement(
                    "label", {"className": "label"}, "Imperial Date Time"
                ),
                React.createElement(
                    "input",
                    {
                        "className": "input",
                        "defaultValue": INITIAL_DATETIME.imdt.year,
                        "name": "imdt.year",
                        "ref": form.register,
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
                        "ref": form.register,
                        "style": {"width": "3.5em"},
                        "type": "number",
                    },
                ),
                React.createElement(
                    "button",
                    {
                        "className": "button is-dark",
                        "onClick": lambda event: draw(form, ref),
                    },
                    "Draw",
                ),
            ),
            React.createElement(
                "div",
                {"className": "field is-grouped"},
                React.createElement(
                    "button",
                    {
                        "className": "button is-dark",
                        "onClick": lambda event: turn_to_previous(form, ref),
                    },
                    "◀",
                ),
                React.createElement(
                    "button",
                    {
                        "className": "button is-dark",
                        "onClick": lambda event: turn_to_next(form, ref),
                    },
                    "▶",
                ),
            ),
        ),
        React.createElement("div", {"ref": ref}),
    )
