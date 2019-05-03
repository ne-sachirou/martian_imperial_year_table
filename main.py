"""Main."""

from imperial_calendar import imperial_date_time_to_sol_number, sol_number_to_imperial_date_time
from imperial_calendar.ImperialDateTime import ImperialDateTime
from imperial_calendar.ImperialSolNumber import ImperialSolNumber
__pragma__("noalias", "clear")
from node_modules.hyperapp.src.index import h, app

__pragma__("skip")
Date = document = Math = 0
__pragma__("noskip")


def new_ref(prefix: str) -> str:
    """Create a React style reference."""
    return f"{prefix}.{Date.now().toString(36)}{Math.random().toString(36).substr(1)}"


def action_sync_by_sol_number(state, event):
    """Action sync_by_sol_number."""
    event.stopPropagation()
    event.preventDefault()
    ref = state["sol_number_ref"]
    sol_number = ImperialSolNumber(float(document.getElementById(ref).value))
    imperial_date_time = sol_number_to_imperial_date_time(state.imperial_sol_number)
    return {"sol_number": sol_number, "imperial_date_time": imperial_date_time}


def action_sync_by_imperial_date_time(state, event):
    """Action sync_by_imperial_date_time."""
    event.stopPropagation()
    event.preventDefault()
    ref = state["imperial_date_time_ref"]
    imperial_date_time = ImperialDateTime(int(document.getElementById(ref + "year").value),
                                          int(document.getElementById(ref + "month").value),
                                          int(document.getElementById(ref + "day").value),
                                          int(document.getElementById(ref + "hour").value),
                                          int(document.getElementById(ref + "minute").value),
                                          int(document.getElementById(ref + "second").value))
    sol_number = imperial_date_time_to_sol_number(imperial_date_time)
    return {"sol_number": sol_number, "imperial_date_time": imperial_date_time}


def view_gregorian_date_time(state, actions):
    """View gregorian_date_time."""
    gregorian_date_time = state["gregorian_date_time"]
    ref = state["gregorian_date_time_ref"]
    return h("div", {"class": "field is-grouped is-grouped-multiline"}, [
        h("label", {
            "class": "label",
            "for": ref + "year"
        }, "Gregorian Date Time"),
        h("input", {
            "id": ref + "year",
            "class": "input",
            "style": {
                "width": "6em"
            },
            "type": "number",
            "value": 0,
        }, ""),
        "-",
        h(
            "input", {
                "id": ref + "month",
                "class": "input",
                "max": 12,
                "min": 1,
                "style": {
                    "width": "3em"
                },
                "type": "number",
                "value": 1,
            }, ""),
        "-",
        h(
            "input", {
                "id": ref + "day",
                "class": "input",
                "max": 31,
                "min": 1,
                "style": {
                    "width": "3em"
                },
                "type": "number",
                "value": 1,
            }, ""),
        "T",
        h("input", {
            "id": ref + "hour",
            "class": "input",
            "style": {
                "width": "3em"
            },
            "type": "number",
            "value": 0
        }, ""),
        ":",
        h("input", {
            "id": ref + "minute",
            "class": "input",
            "style": {
                "width": "3em"
            },
            "type": "number",
            "value": 0,
        }, ""),
        ":",
        h("input", {
            "id": ref + "second",
            "class": "input",
            "style": {
                "width": "3em"
            },
            "type": "number",
            "value": 0
        }, ""),
        h("input", {
            "class": "input",
            "style": {
                "width": "6em"
            },
            "type": "text",
            "value": "+00:00"
        }, ""),
        h("button", {
            "class": "button is-light is-inverted",
            "onclick": lambda event: actions["sync_"](event)
        }, "Sync"),
    ])


def view_julian_day(state, actions):
    """View julian_day."""
    julian_day = state["julian_day"]
    ref = state["julian_day_ref"]
    return h("div", {"class": "field is-grouped"}, [
        h("label", {
            "class": "label",
            "for": ref
        }, "Julian Day"),
        h("input", {
            "id": ref,
            "class": "input",
            "step": 0.00001,
            "type": "number",
            "value": 0,
        }, ""),
        h("button", {
            "class": "button is-light is-inverted",
            "onclick": lambda event: actions["sync_"](event)
        }, "Sync"),
    ])


def view_delta_t(state, actions):
    """View ⊿t."""
    return h("div", {"class": "field is-grouped"}, [h("div", {"class": "label"}, "⊿t"), "0"])


def view_terrestrual_time(state, actions):
    """View terrestrual_time."""
    terrestrual_time = state["terrestrual_time"]
    ref = state["terrestrual_time_ref"]
    return h("div", {"class": "field is-grouped"}, [
        h("label", {
            "class": "label",
            "for": ref
        }, "Terrestrual Time"),
        h("input", {
            "id": ref,
            "class": "input",
            "step": 0.00001,
            "type": "number",
            "value": 0,
        }, ""),
        h("button", {
            "class": "button is-light is-inverted",
            "onclick": lambda event: actions["sync_"](event)
        }, "Sync"),
    ])


def view_areocentric_solar_longitude(state, actions):
    """View areocentric_solar_longitude."""
    areocentric_solar_longitude = state["areocentric_solar_longitude"]
    return h(
        "div", {"class": "field is-grouped"},
        [h("label", {
            "class": "label",
        }, "Areocentric Solar Longitude (Mars Ls)"),
         str(areocentric_solar_longitude)])


def view_mars_sol_date(state, actions):
    """View mars_sol_date."""
    mars_sol_date = state["mars_sol_date"]
    ref = state["mars_sol_date_ref"]
    return h("div", {"class": "field is-grouped"}, [
        h("label", {
            "class": "label",
            "for": ref
        }, "Mars Sol Date"),
        h("input", {
            "id": ref,
            "class": "input",
            "step": 0.00001,
            "type": "number",
            "value": 0,
        }, ""),
        h("button", {
            "class": "button is-light is-inverted",
            "onclick": lambda event: actions["sync_"](event)
        }, "Sync"),
    ])


def view_imperial_sol_number(state, actions):
    """View ImperialSolNumber."""
    sol_number = state["sol_number"]
    ref = state["sol_number_ref"]
    return h("div", {"class": "field is-grouped"}, [
        h("label", {
            "class": "label",
            "for": ref
        }, "Imperial Sol Number"),
        h("input", {
            "id": ref,
            "class": "input",
            "step": 0.00001,
            "type": "number",
            "value": sol_number.imperial_sol_number
        }, ""),
        h("button", {
            "class": "button is-light is-inverted",
            "onclick": lambda event: actions["sync_by_sol_number"](event)
        }, "Sync"),
    ])


def view_imperial_date_time(state, actions):
    """View ImperialDateTime."""
    imperial_date_time = state["imperial_date_time"]
    ref = state["imperial_date_time_ref"]
    return h("div", {"class": "field is-grouped is-grouped-multiline"}, [
        h("label", {
            "class": "label",
            "for": ref + "year"
        }, "Imperial Date Time"),
        h(
            "input", {
                "id": ref + "year",
                "class": "input",
                "style": {
                    "width": "6em"
                },
                "type": "number",
                "value": imperial_date_time.year
            }, ""),
        "-",
        h(
            "input", {
                "id": ref + "month",
                "class": "input",
                "max": 24,
                "min": 1,
                "style": {
                    "width": "3em"
                },
                "type": "number",
                "value": imperial_date_time.month
            }, ""),
        "-",
        h(
            "input", {
                "id": ref + "day",
                "class": "input",
                "max": 28,
                "min": 1,
                "style": {
                    "width": "3em"
                },
                "type": "number",
                "value": imperial_date_time.day
            }, ""),
        "T",
        h(
            "input", {
                "id": ref + "hour",
                "class": "input",
                "style": {
                    "width": "3em"
                },
                "type": "number",
                "value": imperial_date_time.hour
            }, ""),
        ":",
        h(
            "input", {
                "id": ref + "minute",
                "class": "input",
                "style": {
                    "width": "3em"
                },
                "type": "number",
                "value": imperial_date_time.minute
            }, ""),
        ":",
        h(
            "input", {
                "id": ref + "second",
                "class": "input",
                "style": {
                    "width": "3em"
                },
                "type": "number",
                "value": imperial_date_time.second
            }, ""),
        h("input", {
            "class": "input",
            "style": {
                "width": "6em"
            },
            "type": "text",
            "value": "+00:00"
        }, ""),
        h("button", {
            "class": "button is-light is-inverted",
            "onclick": lambda event: actions["sync_by_imperial_date_time"](event)
        }, "Sync"),
    ])


def view(state, actions):
    """View."""
    return h("div", {}, [
        view_gregorian_date_time, view_julian_day, view_delta_t, view_terrestrual_time,
        view_areocentric_solar_longitude, view_mars_sol_date, view_imperial_sol_number, view_imperial_date_time
    ])


def main():
    """Main."""
    sol_number = ImperialSolNumber(0)
    state = {
        "gregorian_date_time": 0,
        "gregorian_date_time_ref": new_ref("gregorian_date_time"),
        "julian_day": 0,
        "julian_day_ref": new_ref("julian_day"),
        "terrestrual_time": 0,
        "terrestrual_time_ref": new_ref("terrestrual_time"),
        "areocentric_solar_longitude": 0.00001,
        "mars_sol_date": 0,
        "mars_sol_date_ref": new_ref("mars_sol_date"),
        "sol_number": sol_number,
        "sol_number_ref": new_ref("sol_number"),
        "imperial_date_time": sol_number_to_imperial_date_time(sol_number),
        "imperial_date_time_ref": new_ref("imperial_date_time")
    }
    actions = {
        "sync_by_sol_number": lambda event: lambda state: action_sync_by_sol_number(state, event),
        "sync_by_imperial_date_time": lambda event: lambda state: action_sync_by_imperial_date_time(state, event),
    }
    app(state, actions, view, document.getElementById("app"))
