"""UI global navigation view."""
from node_modules.hyperapp.src.index import h  # type: ignore


def view_global_navigation(state, actions):
    """UI global navigation view."""
    navbar_tab_items = []
    for (main_content, href, title) in [
        ("transform", "/", "變換"),
        ("description", "/description", "解説"),
    ]:
        klass = ["is-tab", "navbar-item"]
        if state["global_navigation"]["main_content"] == main_content:
            klass.append("is-active")
        navbar_tab_item = h(
            "a",
            {
                "class": " ".join(klass),
                "data-main-content": main_content,
                "href": href,
                "onclick": lambda event: actions["global_navigation"][
                    "switch_main_content"
                ](event),
            },
            title,
        )
        navbar_tab_items.append(navbar_tab_item)
    if state["global_navigation"]["is_active"]:
        navbar_menu_is_active = " is-active "
    else:
        navbar_menu_is_active = ""
    return h(
        "nav",
        {"aria-label": "main navigation", "class": "navbar", "role": "navigation"},
        [
            h(
                "div",
                {"class": "navbar-brand"},
                [
                    h(
                        "h1",
                        {"class": "navbar-item"},
                        [
                            h(
                                "img",
                                {
                                    "alt": "帝國火星暦",
                                    "src": "/static/img/martian_empire.png",
                                },
                                [],
                            ),
                            h("div", {}, "帝國火星暦"),
                        ],
                    ),
                    h(
                        "a",
                        {
                            "aria-expanded": "false",
                            "aria-label": "menu",
                            "class": "navbar-burger" + navbar_menu_is_active,
                            "onclick": lambda event: actions["global_navigation"][
                                "toggle_navbar_menu"
                            ](event),
                            "role": "button",
                        },
                        [h("span", {"aria-hidden": "true"}, "") for i in range(0, 3)],
                    ),
                ],
            ),
            h(
                "div",
                {"class": "navbar-menu" + navbar_menu_is_active},
                [
                    h("div", {"class": "navbar-start"}, navbar_tab_items),
                    h(
                        "div",
                        {"class": "navbar-end"},
                        [
                            h(
                                "a",
                                {
                                    "class": "navbar-item",
                                    "href": "https://github.com/ne-sachirou/martian_imperial_year_table",
                                    "title": "GitHub",
                                },
                                [
                                    h(
                                        "img",
                                        {
                                            "alt": "GitHub",
                                            "src": "/static/img/GitHub-Mark-120px-plus.png",
                                        },
                                        [],
                                    )
                                ],
                            )
                        ],
                    ),
                ],
            ),
        ],
    )
