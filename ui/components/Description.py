"""Description component."""
from ui.Api import Api
import typing as t

__pragma__(  # noqa: F821
    "js",
    "{}",
    """
    const React = require("react");
    """,
)

React: t.Any = 0  # __:skip
document: t.Any = 0  # __:skip
js_undefined: t.Any = 0  # __:skip


# (a.{~(48+i.10),(97+i.26),(65+i.26)){~]32?@$62
ref = "OQeicebRkj87J29D6erS7BMKzuysRV6k"


async def fetch_description(html: str, set_html) -> None:
    """Fetch the description from the Web API."""
    if html is not None:
        return
    description = await Api().get_description()
    set_html(description.html)


def use_description() -> str:
    """Provide a hook to fetch thr description."""
    [html, set_html] = React.useState(None)
    React.useEffect(lambda: fetch_description(html, set_html) and js_undefined)
    return html


def draw_description(html: str) -> None:
    """Draw the description HTML."""
    if html is not None:
        document.getElementById(ref).innerHTML = html


def Description(props: dict):
    """Render a Description component."""
    html = use_description()
    React.useEffect(lambda: draw_description(html), [html])
    return React.createElement("div", {"id": ref, "className": "content section"})
