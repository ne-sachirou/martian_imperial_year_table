"""Main."""
from node_modules.hyperapp.src.index import app  # type: ignore
import typing as t
from ui.actions import actions
from ui.initial_state import initial_state
from ui.view import view

document: t.Any = 0  # __:skip
setTimeout: t.Any = 0  # __:skip


def main():
    """UI Main."""
    main = app(initial_state(), actions(), view, document.getElementById("app"))
    setTimeout(lambda: main["transform"]["sync_by_grdt"](None), 0)
