"""UI transform view."""
from node_modules.hyperapp.src.index import h  # type: ignore


def view_grdt(state, actions):
    """View grdt."""
    grdt = state["transform"]["grdt"]
    return h(
        "div",
        {"class": "field is-grouped is-grouped-multiline"},
        [
            h("label", {"class": "label"}, "Gregorian Date Time"),
            h(
                "input",
                {
                    "class": "input",
                    "oninput": lambda event: actions["transform"]["change_grdt_year"](
                        event
                    ),
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
                    "class": "input",
                    "max": 12,
                    "min": 1,
                    "oninput": lambda event: actions["transform"]["change_grdt_month"](
                        event
                    ),
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
                    "class": "input",
                    "max": 31,
                    "min": 1,
                    "oninput": lambda event: actions["transform"]["change_grdt_day"](
                        event
                    ),
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
                    "class": "input",
                    "oninput": lambda event: actions["transform"]["change_grdt_hour"](
                        event
                    ),
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
                    "class": "input",
                    "oninput": lambda event: actions["transform"]["change_grdt_minute"](
                        event
                    ),
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
                    "class": "input",
                    "oninput": lambda event: actions["transform"]["change_grdt_second"](
                        event
                    ),
                    "style": {"width": "3.5em"},
                    "type": "number",
                    "value": grdt.second,
                },
                "",
            ),
            h(
                "input",
                {
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
    return h(
        "div",
        {"class": "field is-grouped"},
        [
            h("label", {"class": "label"}, "Julian Day"),
            h(
                "input",
                {
                    "class": "input",
                    "oninput": lambda event: actions["transform"]["change_juld"](event),
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
    return h(
        "div",
        {"class": "field is-grouped"},
        [
            h("label", {"class": "label"}, "Terrestrial Time"),
            h(
                "input",
                {
                    "class": "input",
                    "oninput": lambda event: actions["transform"]["change_tert"](event),
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
    return h(
        "div",
        {"class": "field is-grouped"},
        [
            h("label", {"class": "label"}, "Mars Sol Date"),
            h(
                "input",
                {
                    "class": "input",
                    "oninput": lambda event: actions["transform"]["change_mrsd"](event),
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
    return h(
        "div",
        {"class": "field is-grouped"},
        [
            h("label", {"class": "label"}, "Imperial Sol Number"),
            h(
                "input",
                {
                    "class": "input",
                    "oninput": lambda event: actions["transform"]["change_imsn"](event),
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
    return h(
        "div",
        {"class": "field is-grouped is-grouped-multiline"},
        [
            h("label", {"class": "label"}, "Imperial Date Time"),
            h(
                "input",
                {
                    "class": "input",
                    "oninput": lambda event: actions["transform"]["change_imdt_year"](
                        event
                    ),
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
                    "class": "input",
                    "max": 24,
                    "min": 1,
                    "oninput": lambda event: actions["transform"]["change_imdt_month"](
                        event
                    ),
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
                    "class": "input",
                    "max": 28,
                    "min": 1,
                    "oninput": lambda event: actions["transform"]["change_imdt_day"](
                        event
                    ),
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
                    "class": "input",
                    "oninput": lambda event: actions["transform"]["change_imdt_hour"](
                        event
                    ),
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
                    "class": "input",
                    "oninput": lambda event: actions["transform"]["change_imdt_minute"](
                        event
                    ),
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
                    "class": "input",
                    "oninput": lambda event: actions["transform"]["change_imdt_second"](
                        event
                    ),
                    "style": {"width": "3.5em"},
                    "type": "number",
                    "value": imdt.second,
                },
                "",
            ),
            h(
                "input",
                {
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
