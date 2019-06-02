"""Main."""

from imperial_calendar import *
from imperial_calendar.transform import *

__pragma__("noalias", "clear")  # type: ignore
from node_modules.hyperapp.src.index import h, app  # type: ignore

__pragma__("skip")  # type: ignore
Date = document = Math = 0
__pragma__("noskip")  # type: ignore


def new_ref(prefix: str) -> str:
    """Create a React style reference."""
    # fmt: off
    ref = f"{prefix}.{Date.now().toString(36)}{Math.random().toString(36).substr(1)}" # type: ignore
    # fmt: on
    return ref


def action_sync_by_grdt(state, event):
    """Action sync_by_grdt."""
    event.stopPropagation()
    event.preventDefault()
    ref = state["grdt_ref"]
    grdt = GregorianDateTime(
        int(document.getElementById(ref + "year").value),
        int(document.getElementById(ref + "month").value),
        int(document.getElementById(ref + "day").value),
        int(document.getElementById(ref + "hour").value),
        int(document.getElementById(ref + "minute").value),
        int(document.getElementById(ref + "second").value),
        GregorianDateTime.parse_timezone_str(
            document.getElementById(ref + "timezone").value
        ),
    )
    juld = grdt_to_juld(grdt)
    tert = juld_to_tert(juld)
    mrsd = tert_to_mrsd(tert)
    imsn = mrsd_to_imsn(mrsd)
    imdt = imsn_to_imdt(imsn, 0.0)
    return {
        "grdt": grdt,
        "juld": juld,
        "tert": tert,
        "mrsd": mrsd,
        "imsn": imsn,
        "imdt": imdt,
    }


def action_sync_by_juld(state, event):
    """Action sync_by_juld."""
    event.stopPropagation()
    event.preventDefault()
    ref = state["juld_ref"]
    juld = JulianDay(float(document.getElementById(ref).value))
    grdt = juld_to_grdt(juld, 0.0)
    tert = juld_to_tert(juld)
    mrsd = tert_to_mrsd(tert)
    imsn = mrsd_to_imsn(mrsd)
    imdt = imsn_to_imdt(imsn, 0.0)
    return {
        "grdt": grdt,
        "juld": juld,
        "tert": tert,
        "mrsd": mrsd,
        "imsn": imsn,
        "imdt": imdt,
    }


def action_sync_by_tert(state, event):
    """Action sync_by_tert."""
    event.stopPropagation()
    event.preventDefault()
    ref = state["tert_ref"]
    tert = TerrestrialTime(float(document.getElementById(ref).value))
    juld = tert_to_juld(tert)
    grdt = juld_to_grdt(juld, 0.0)
    mrsd = tert_to_mrsd(tert)
    imsn = mrsd_to_imsn(mrsd)
    imdt = imsn_to_imdt(imsn, 0.0)
    return {
        "grdt": grdt,
        "juld": juld,
        "tert": tert,
        "mrsd": mrsd,
        "imsn": imsn,
        "imdt": imdt,
    }


def action_sync_by_mrsd(state, event):
    """Action sync_by_mrsd."""
    event.stopPropagation()
    event.preventDefault()
    ref = state["mrsd_ref"]
    mrsd = MarsSolDate(float(document.getElementById(ref).value))
    tert = mrsd_to_tert(mrsd)
    juld = tert_to_juld(tert)
    grdt = juld_to_grdt(juld, 0.0)
    imsn = mrsd_to_imsn(mrsd)
    imdt = imsn_to_imdt(imsn, 0.0)
    return {
        "grdt": grdt,
        "juld": juld,
        "tert": tert,
        "mrsd": mrsd,
        "imsn": imsn,
        "imdt": imdt,
    }


def action_sync_by_imsn(state, event):
    """Action sync_by_imsn."""
    event.stopPropagation()
    event.preventDefault()
    ref = state["imsn_ref"]
    imsn = ImperialSolNumber(float(document.getElementById(ref).value))
    mrsd = imsn_to_mrsd(imsn)
    tert = mrsd_to_tert(mrsd)
    juld = tert_to_juld(tert)
    grdt = juld_to_grdt(juld, 0.0)
    imdt = imsn_to_imdt(imsn, 0.0)
    return {
        "grdt": grdt,
        "juld": juld,
        "tert": tert,
        "mrsd": mrsd,
        "imsn": imsn,
        "imdt": imdt,
    }


def action_sync_by_imdt(state, event):
    """Action sync_by_imdt."""
    event.stopPropagation()
    event.preventDefault()
    ref = state["imdt_ref"]
    imdt = ImperialDateTime(
        int(document.getElementById(ref + "year").value),
        int(document.getElementById(ref + "month").value),
        int(document.getElementById(ref + "day").value),
        int(document.getElementById(ref + "hour").value),
        int(document.getElementById(ref + "minute").value),
        int(document.getElementById(ref + "second").value),
        ImperialDateTime.parse_timezone_str(
            document.getElementById(ref + "timezone").value
        ),
    )
    imsn = imdt_to_imsn(imdt)
    mrsd = imsn_to_mrsd(imsn)
    tert = mrsd_to_tert(mrsd)
    juld = tert_to_juld(tert)
    grdt = juld_to_grdt(juld, 0.0)
    return {
        "grdt": grdt,
        "juld": juld,
        "tert": tert,
        "mrsd": mrsd,
        "imsn": imsn,
        "imdt": imdt,
    }


def view_grdt(state, actions):
    """View grdt."""
    grdt = state["grdt"]
    ref = state["grdt_ref"]
    return h(
        "div",
        {"class": "field is-grouped is-grouped-multiline"},
        [
            h("label", {"class": "label", "for": ref + "year"}, "Gregorian Date Time"),
            h(
                "input",
                {
                    "id": ref + "year",
                    "class": "input",
                    "style": {"width": "6em"},
                    "type": "number",
                    "value": grdt.year,
                },
                "",
            ),
            "-",
            h(
                "input",
                {
                    "id": ref + "month",
                    "class": "input",
                    "max": 12,
                    "min": 1,
                    "style": {"width": "3.5em"},
                    "type": "number",
                    "value": grdt.month,
                },
                "",
            ),
            "-",
            h(
                "input",
                {
                    "id": ref + "day",
                    "class": "input",
                    "max": 31,
                    "min": 1,
                    "style": {"width": "3.5em"},
                    "type": "number",
                    "value": grdt.day,
                },
                "",
            ),
            "T",
            h(
                "input",
                {
                    "id": ref + "hour",
                    "class": "input",
                    "style": {"width": "3.5em"},
                    "type": "number",
                    "value": grdt.hour,
                },
                "",
            ),
            ":",
            h(
                "input",
                {
                    "id": ref + "minute",
                    "class": "input",
                    "style": {"width": "3.5em"},
                    "type": "number",
                    "value": grdt.minute,
                },
                "",
            ),
            ":",
            h(
                "input",
                {
                    "id": ref + "second",
                    "class": "input",
                    "style": {"width": "3.5em"},
                    "type": "number",
                    "value": grdt.second,
                },
                "",
            ),
            h(
                "input",
                {
                    "id": ref + "timezone",
                    "class": "input",
                    "style": {"width": "6em"},
                    "type": "text",
                    "value": grdt.timezone_str,
                },
                "",
            ),
            h(
                "button",
                {
                    "class": "button is-dark",
                    "onclick": lambda event: actions["sync_by_grdt"](event),
                },
                "Sync",
            ),
        ],
    )


def view_juld(state, actions):
    """View juld."""
    juld = state["juld"]
    ref = state["juld_ref"]
    return h(
        "div",
        {"class": "field is-grouped"},
        [
            h("label", {"class": "label", "for": ref}, "Julian Day"),
            h(
                "input",
                {
                    "id": ref,
                    "class": "input",
                    "step": 0.00001,
                    "type": "number",
                    "value": juld.julian_day,
                },
                "",
            ),
            h(
                "button",
                {
                    "class": "button is-dark",
                    "onclick": lambda event: actions["sync_by_juld"](event),
                },
                "Sync",
            ),
        ],
    )


def view_delta_t(state, actions):
    """View ⊿t."""
    juld = state["juld"]
    return h(
        "div",
        {"class": "field is-grouped"},
        [h("div", {"class": "label"}, "⊿t"), str(juld.delta_t)],
    )


def view_tert(state, actions):
    """View tert."""
    tert = state["tert"]
    ref = state["tert_ref"]
    return h(
        "div",
        {"class": "field is-grouped"},
        [
            h("label", {"class": "label", "for": ref}, "Terrestrual Time"),
            h(
                "input",
                {
                    "id": ref,
                    "class": "input",
                    "step": 0.00001,
                    "type": "number",
                    "value": tert.terrestrial_time,
                },
                "",
            ),
            h(
                "button",
                {
                    "class": "button is-dark",
                    "onclick": lambda event: actions["sync_by_tert"](event),
                },
                "Sync",
            ),
        ],
    )


def view_mrls(state, actions):
    """View mrls."""
    tert = state["tert"]
    mrls = tert_to_mrls(tert)
    return h(
        "div",
        {"class": "field is-grouped"},
        [
            h("label", {"class": "label"}, "Areocentric Solar Longitude (Mars Ls)"),
            str(mrls),
        ],
    )


def view_mrsd(state, actions):
    """View mrsd."""
    mrsd = state["mrsd"]
    ref = state["mrsd_ref"]
    return h(
        "div",
        {"class": "field is-grouped"},
        [
            h("label", {"class": "label", "for": ref}, "Mars Sol Date"),
            h(
                "input",
                {
                    "id": ref,
                    "class": "input",
                    "step": 0.00001,
                    "type": "number",
                    "value": mrsd.mars_sol_date,
                },
                "",
            ),
            h(
                "button",
                {
                    "class": "button is-dark",
                    "onclick": lambda event: actions["sync_by_mrsd"](event),
                },
                "Sync",
            ),
        ],
    )


def view_imperial_imsn(state, actions):
    """View ImperialSolNumber."""
    imsn = state["imsn"]
    ref = state["imsn_ref"]
    return h(
        "div",
        {"class": "field is-grouped"},
        [
            h("label", {"class": "label", "for": ref}, "Imperial Sol Number"),
            h(
                "input",
                {
                    "id": ref,
                    "class": "input",
                    "step": 0.00001,
                    "type": "number",
                    "value": imsn.imperial_sol_number,
                },
                "",
            ),
            h(
                "button",
                {
                    "class": "button is-dark",
                    "onclick": lambda event: actions["sync_by_imsn"](event),
                },
                "Sync",
            ),
        ],
    )


def view_imdt(state, actions):
    """View ImperialDateTime."""
    imdt = state["imdt"]
    ref = state["imdt_ref"]
    return h(
        "div",
        {"class": "field is-grouped is-grouped-multiline"},
        [
            h("label", {"class": "label", "for": ref + "year"}, "Imperial Date Time"),
            h(
                "input",
                {
                    "id": ref + "year",
                    "class": "input",
                    "style": {"width": "6em"},
                    "type": "number",
                    "value": imdt.year,
                },
                "",
            ),
            "-",
            h(
                "input",
                {
                    "id": ref + "month",
                    "class": "input",
                    "max": 24,
                    "min": 1,
                    "style": {"width": "3.5em"},
                    "type": "number",
                    "value": imdt.month,
                },
                "",
            ),
            "-",
            h(
                "input",
                {
                    "id": ref + "day",
                    "class": "input",
                    "max": 28,
                    "min": 1,
                    "style": {"width": "3.5em"},
                    "type": "number",
                    "value": imdt.day,
                },
                "",
            ),
            "T",
            h(
                "input",
                {
                    "id": ref + "hour",
                    "class": "input",
                    "style": {"width": "3.5em"},
                    "type": "number",
                    "value": imdt.hour,
                },
                "",
            ),
            ":",
            h(
                "input",
                {
                    "id": ref + "minute",
                    "class": "input",
                    "style": {"width": "3.5em"},
                    "type": "number",
                    "value": imdt.minute,
                },
                "",
            ),
            ":",
            h(
                "input",
                {
                    "id": ref + "second",
                    "class": "input",
                    "style": {"width": "3.5em"},
                    "type": "number",
                    "value": imdt.second,
                },
                "",
            ),
            h(
                "input",
                {
                    "id": ref + "timezone",
                    "class": "input",
                    "style": {"width": "6em"},
                    "type": "text",
                    "value": imdt.timezone_str,
                },
                "",
            ),
            h(
                "button",
                {
                    "class": "button is-dark",
                    "onclick": lambda event: actions["sync_by_imdt"](event),
                },
                "Sync",
            ),
        ],
    )


def view(state, actions):
    """View."""
    return h(
        "div",
        {},
        [
            view_grdt,
            view_juld,
            view_delta_t,
            view_tert,
            view_mrls,
            view_mrsd,
            view_imperial_imsn,
            view_imdt,
        ],
    )


def main():
    """Main."""
    grdt = GregorianDateTime(0, 1, 1, 0, 0, 0, 0.0)
    juld = grdt_to_juld(grdt)
    tert = juld_to_tert(juld)
    mrsd = tert_to_mrsd(tert)
    imsn = mrsd_to_imsn(mrsd)
    imdt = imsn_to_imdt(imsn, 0.0)
    state = {
        "grdt": grdt,
        "grdt_ref": new_ref("grdt"),
        "juld": juld,
        "juld_ref": new_ref("juld"),
        "tert": tert,
        "tert_ref": new_ref("tert"),
        "mrsd": mrsd,
        "mrsd_ref": new_ref("mrsd"),
        "imsn": imsn,
        "imsn_ref": new_ref("imsn"),
        "imdt": imdt,
        "imdt_ref": new_ref("imdt"),
    }
    actions = {
        "sync_by_grdt": lambda event: lambda state: action_sync_by_grdt(state, event),
        "sync_by_juld": lambda event: lambda state: action_sync_by_juld(state, event),
        "sync_by_tert": lambda event: lambda state: action_sync_by_tert(state, event),
        "sync_by_mrsd": lambda event: lambda state: action_sync_by_mrsd(state, event),
        "sync_by_imsn": lambda event: lambda state: action_sync_by_imsn(state, event),
        "sync_by_imdt": lambda event: lambda state: action_sync_by_imdt(state, event),
    }
    app(state, actions, view, document.getElementById("app"))
