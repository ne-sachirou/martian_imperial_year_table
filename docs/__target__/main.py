"""Main."""

from martian_calendar import sol_number_to_martian_date_time
from martian_calendar.SolNumber import SolNumber
__pragma__("noalias", "clear")
from node_modules.hyperapp.src.index import h, app


__pragma__("skip")
document = Math = 0
__pragma__("noskip")


def action_sol_number_to_martian_date_time(state, event):
    "Action sol_number_to_martian_date_time."
    event.stopPropagation()
    event.preventDefault()
    return {"sol_number": SolNumber(float(document.getElementById(state["sol_number_ref"]).value))}


def view(state, actions):
    """View."""
    martian_date_time = sol_number_to_martian_date_time(state.sol_number)
    return h("div", {}, [
        h("form", {}, [
            h("div", {}, [
                h("label", {"for": state["sol_number_ref"]}, "SolNumber: "),
                h("input", {"id": state["sol_number_ref"], "step": "0.00001", "type": "number", "value": state["sol_number"].sol_number}, "")
            ]),
            h("button", {"onclick": lambda event: actions["sol_number_to_martian_date_time"](event)}, "to MartianDateTime")
        ]),
        h("div", {}, f"MartianDateTime: {martian_date_time.year}-{martian_date_time.month}-{martian_date_time.day}T{martian_date_time.hour}:{martian_date_time.hour}:{martian_date_time.second}")
    ])


def main():
    """Main."""
    state = {
        "sol_number": SolNumber(0),
        "sol_number_ref": "sol_number_ref" + Math.random()
    }
    actions = {
        "sol_number_to_martian_date_time": lambda event: lambda state: action_sol_number_to_martian_date_time(state, event)
    }
    app(state, actions, view, document.getElementById("app"))
