"""Main."""

from imperial_calendar import imperial_date_time_to_sol_number, sol_number_to_imperial_date_time
from imperial_calendar.ImperialDateTime import ImperialDateTime
from imperial_calendar.SolNumber import SolNumber
__pragma__("noalias", "clear")
from node_modules.hyperapp.src.index import h, app

__pragma__("skip")
document = Math = 0
__pragma__("noskip")


def action_sync_by_sol_number(state, event):
    "Action sync_by_sol_number."
    event.stopPropagation()
    event.preventDefault()
    ref = state["sol_number_ref"]
    sol_number = SolNumber(float(document.getElementById(ref).value))
    imperial_date_time = sol_number_to_imperial_date_time(state.sol_number)
    return {"sol_number": sol_number, "imperial_date_time": imperial_date_time}


def action_sync_by_imperial_date_time(state, event):
    "Action sync_by_imperial_date_time."
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


def view_sol_number(state, actions):
    "View SolNumber."
    return h("div", {}, [
        h("label", {"for": state["sol_number_ref"]}, "SolNumber: "),
        h("input", {
            "id": state["sol_number_ref"],
            "step": "0.00001",
            "type": "number",
            "value": state["sol_number"].sol_number
        }, ""),
        h("button", {"onclick": lambda event: actions["sync_by_sol_number"](event)}, "Sync"),
    ])


def view_imperial_date_time(state, actions):
    "View ImperialDateTime."
    imperial_date_time = state["imperial_date_time"]
    ref = state["imperial_date_time_ref"]
    return h("div", {}, [
        h("label", {"for": ref + "year"}, "ImperialDateTime: "),
        h("input", {
            "id": ref + "year",
            "type": "number",
            "value": imperial_date_time.year
        }, ""),
        "-",
        h("input", {
            "id": ref + "month",
            "type": "number",
            "value": imperial_date_time.month
        }, ""),
        "-",
        h("input", {
            "id": ref + "day",
            "type": "number",
            "value": imperial_date_time.day
        }, ""),
        "T",
        h("input", {
            "id": ref + "hour",
            "type": "number",
            "value": imperial_date_time.hour
        }, ""),
        ":",
        h("input", {
            "id": ref + "minute",
            "type": "number",
            "value": imperial_date_time.minute
        }, ""),
        ":",
        h("input", {
            "id": ref + "second",
            "type": "number",
            "value": imperial_date_time.second
        }, ""),
        h("button", {"onclick": lambda event: actions["sync_by_imperial_date_time"](event)}, "Sync"),
    ])


def view(state, actions):
    """View."""
    return h("div", {}, [view_sol_number, view_imperial_date_time])


def main():
    """Main."""
    sol_number = SolNumber(0)
    state = {
        "sol_number": sol_number,
        "sol_number_ref": "sol_number" + Math.random().toString(36),
        "imperial_date_time": sol_number_to_imperial_date_time(sol_number),
        "imperial_date_time_ref": "imperial_date_time" + Math.random().toString(36),
    }
    actions = {
        "sync_by_sol_number": lambda event: lambda state: action_sync_by_sol_number(state, event),
        "sync_by_imperial_date_time": lambda event: lambda state: action_sync_by_imperial_date_time(state, event),
    }
    app(state, actions, view, document.getElementById("app"))
