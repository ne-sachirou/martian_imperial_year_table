"""UI transform view."""
from node_modules.hyperapp.src.index import h  # type: ignore


def view_grdt(state, actions):
    """View grdt."""
    grdt = state["transform"]["grdt"]
    ref = state["transform"]["grdt_ref"]
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
                    "oninput": lambda event: actions["transform"][
                        "change_grdt_timezone"
                    ](event),
                    "style": {"width": "6em"},
                    "type": "text",
                    "value": grdt.timezone,
                },
                "",
            ),
            h(
                "button",
                {
                    "class": "button is-dark",
                    "onclick": lambda event: actions["transform"]["sync_by_grdt"](
                        event
                    ),
                },
                "Sync",
            ),
        ],
    )


def view_juld(state, actions):
    """View juld."""
    juld = state["transform"]["juld"]
    ref = state["transform"]["juld_ref"]
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
                    "value": round(juld.julian_day, 5),
                },
                "",
            ),
            h(
                "button",
                {
                    "class": "button is-dark",
                    "onclick": lambda event: actions["transform"]["sync_by_juld"](
                        event
                    ),
                },
                "Sync",
            ),
        ],
    )


def view_delta_t(state, actions):
    """View ⊿t."""
    delta_t = state["transform"]["delta_t"]
    return h(
        "div",
        {"class": "field is-grouped"},
        [h("div", {"class": "label"}, "⊿t"), str(round(delta_t, 5))],
    )


def view_tert(state, actions):
    """View tert."""
    tert = state["transform"]["tert"]
    ref = state["transform"]["tert_ref"]
    return h(
        "div",
        {"class": "field is-grouped"},
        [
            h("label", {"class": "label", "for": ref}, "Terrestrial Time"),
            h(
                "input",
                {
                    "id": ref,
                    "class": "input",
                    "step": 0.00001,
                    "type": "number",
                    "value": round(tert.terrestrial_time, 5),
                },
                "",
            ),
            h(
                "button",
                {
                    "class": "button is-dark",
                    "onclick": lambda event: actions["transform"]["sync_by_tert"](
                        event
                    ),
                },
                "Sync",
            ),
        ],
    )


def view_mrls(state, actions):
    """View mrls."""
    mrls = state["transform"]["mrls"]
    return h(
        "div",
        {"class": "field is-grouped"},
        [
            h("label", {"class": "label"}, "Areocentric Solar Longitude (Mars Ls)"),
            str(round(mrls, 5)),
        ],
    )


def view_mrsd(state, actions):
    """View mrsd."""
    mrsd = state["transform"]["mrsd"]
    ref = state["transform"]["mrsd_ref"]
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
                    "value": round(mrsd.mars_sol_date, 5),
                },
                "",
            ),
            h(
                "button",
                {
                    "class": "button is-dark",
                    "onclick": lambda event: actions["transform"]["sync_by_mrsd"](
                        event
                    ),
                },
                "Sync",
            ),
        ],
    )


def view_imsn(state, actions):
    """View ImperialSolNumber."""
    imsn = state["transform"]["imsn"]
    ref = state["transform"]["imsn_ref"]
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
                    "value": round(imsn.imperial_sol_number, 5),
                },
                "",
            ),
            h(
                "button",
                {
                    "class": "button is-dark",
                    "onclick": lambda event: actions["transform"]["sync_by_imsn"](
                        event
                    ),
                },
                "Sync",
            ),
        ],
    )


def view_imdt(state, actions):
    """View ImperialDateTime."""
    imdt = state["transform"]["imdt"]
    ref = state["transform"]["imdt_ref"]
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
                    "oninput": lambda event: actions["transform"][
                        "change_imdt_timezone"
                    ](event),
                    "style": {"width": "6em"},
                    "type": "text",
                    "value": imdt.timezone,
                },
                "",
            ),
            h(
                "button",
                {
                    "class": "button is-dark",
                    "onclick": lambda event: actions["transform"]["sync_by_imdt"](
                        event
                    ),
                },
                "Sync",
            ),
        ],
    )


def view_transform(state, actions):
    """UI transform view."""
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
            view_imsn,
            view_imdt,
        ],
    )
