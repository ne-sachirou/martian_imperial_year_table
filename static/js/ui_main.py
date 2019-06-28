"""Main."""
from node_modules.hyperapp.src.index import app  # type: ignore
from ui.actions import actions
from ui.initial_state import initial_state
from ui.view import view

document = setTimeout = 0  # __:skip


def main():
    """Main."""
    main = app(initial_state(), actions(), view, document.getElementById("app"))
    setTimeout(lambda: main["sync_by_grdt"](None), 0)
