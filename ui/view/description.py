"""UI description view."""
from node_modules.hyperapp.src.index import h  # type: ignore
import typing as t

# __pragma__("skip")
document: t.Any = 0
setTimeout: t.Any = 0
# __pragma__("noskip")


def draw_description(ref: str, content: str) -> None:
    """Draw the description content."""
    document.getElementById(ref).innerHTML = content


def view_description(state, actions):
    """UI description view."""
    content: t.Optional[str] = state["description"]["content"]
    ref: str = state["description"]["ref"]
    if not content:
        actions["description"]["fetch_description"](None)
        return h(
            "div", {"class": "content section", "id": ref}, [h("h1", {}, "帝國火星曆に就て")]
        )
    setTimeout(lambda: draw_description(ref, content), 10)
    return h(
        "section", {"class": "content section", "id": ref}, [h("h1", {}, "帝國火星曆に就て")]
    )
