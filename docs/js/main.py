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
    sol_number = SolNumber(float(document.getElementById(state["sol_number_ref"]).value))
    imperial_date_time = sol_number_to_imperial_date_time(state.sol_number)
    return {"sol_number": sol_number, "imperial_date_time": imperial_date_time}


def action_sync_by_imperial_date_time(state, event):
    "Action sync_by_imperial_date_time."
    event.stopPropagation()
    event.preventDefault()
    imperial_date_time = ImperialDateTime(int(document.getElementById(state["imperial_date_time_year_ref"]).value),
                                          int(document.getElementById(state["imperial_date_time_month_ref"]).value),
                                          int(document.getElementById(state["imperial_date_time_day_ref"]).value),
                                          int(document.getElementById(state["imperial_date_time_hour_ref"]).value),
                                          int(document.getElementById(state["imperial_date_time_minute_ref"]).value),
                                          int(document.getElementById(state["imperial_date_time_second_ref"]).value))
    sol_number = imperial_date_time_to_sol_number(imperial_date_time)
    return {"sol_number": sol_number, "imperial_date_time": imperial_date_time}


def view(state, actions):
    """View."""
    return h("div", {}, [
        h("div", {}, [
            h("label", {"for": state["sol_number_ref"]}, "SolNumber: "),
            h("input", {
                "id": state["sol_number_ref"],
                "step": "0.00001",
                "type": "number",
                "value": state["sol_number"].sol_number
            }, ""),
            h("button", {"onclick": lambda event: actions["sync_by_sol_number"](event)}, "Sync"),
        ]),
        h("div", {}, [
            h("label", {"for": state["imperial_date_time_year_ref"]}, "ImperialDateTime: "),
            h("input", {
                "id": state["imperial_date_time_year_ref"],
                "type": "number",
                "value": state["imperial_date_time"].year
            }, ""),
            h("span", {}, "-"),
            h("input", {
                "id": state["imperial_date_time_month_ref"],
                "type": "number",
                "value": state["imperial_date_time"].month
            }, ""),
            h("span", {}, "-"),
            h("input", {
                "id": state["imperial_date_time_day_ref"],
                "type": "number",
                "value": state["imperial_date_time"].day
            }, ""),
            h("span", {}, "T"),
            h("input", {
                "id": state["imperial_date_time_hour_ref"],
                "type": "number",
                "value": state["imperial_date_time"].hour
            }, ""),
            h("span", {}, ":"),
            h("input", {
                "id": state["imperial_date_time_minute_ref"],
                "type": "number",
                "value": state["imperial_date_time"].minute
            }, ""),
            h("span", {}, ":"),
            h("input", {
                "id": state["imperial_date_time_second_ref"],
                "type": "number",
                "value": state["imperial_date_time"].second
            }, ""),
            h("button", {"onclick": lambda event: actions["sync_by_imperial_date_time"](event)}, "Sync"),
        ])
    ])


def main():
    """Main."""
    sol_number = SolNumber(0)
    state = {
        "sol_number": sol_number,
        "sol_number_ref": "sol_number" + Math.random(),
        "imperial_date_time": sol_number_to_imperial_date_time(sol_number),
        "imperial_date_time_year_ref": "imperial_date_time_year" + Math.random(),
        "imperial_date_time_month_ref": "imperial_date_time_month" + Math.random(),
        "imperial_date_time_day_ref": "imperial_date_time_day" + Math.random(),
        "imperial_date_time_hour_ref": "imperial_date_time_hour" + Math.random(),
        "imperial_date_time_minute_ref": "imperial_date_time_minute" + Math.random(),
        "imperial_date_time_second_ref": "imperial_date_time_second" + Math.random(),
    }
    actions = {
        "sync_by_sol_number": lambda event: lambda state: action_sync_by_sol_number(state, event),
        "sync_by_imperial_date_time": lambda event: lambda state: action_sync_by_imperial_date_time(state, event),
    }
    app(state, actions, view, document.getElementById("app"))
